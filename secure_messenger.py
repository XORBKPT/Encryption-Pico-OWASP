#!/usr/bin/env python3
"""
Secure Offline Messaging System for Raspberry Pi Zero
Designed for engineers in high-voltage environments.
Compliant with ISO/IEC 27001, OWASP, and NIST standards.
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import qrcode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import configparser
import logging
import os
import base64

# Setup logging for security auditing
logging.basicConfig(filename='/var/log/secure_messenger.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')
logging.info("Secure Messenger started")

# Load configuration securely
config = configparser.ConfigParser()
try:
    config.read('/home/pi/config.ini')
except Exception as e:
    logging.error(f"Failed to read config.ini: {e}")
    exit(1)

# Encryption variables (loaded from config.ini)
KEY = base64.b64decode(config['ENCRYPTION']['key'])
IV = base64.b64decode(config['ENCRYPTION']['iv'])

# Validate key and IV lengths
if len(KEY) != 32 or len(IV) != 16:
    logging.error("Invalid key or IV length in config.ini")
    exit(1)

def encrypt_message(message):
    """Encrypt message with AES-256-CBC and PKCS7 padding."""
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    padded_message = pad(message.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return base64.b64encode(ciphertext).decode()

def generate_qr_code(encrypted_message):
    """Generate a QR code from the encrypted message."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(encrypted_message)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("/tmp/qr_code.png")

def on_generate():
    """Handle message input and QR code generation."""
    message = message_entry.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Error", "Message cannot be empty")
        return
    if len(message) > 256:
        messagebox.showerror("Error", "Message must be 256 characters or less")
        return
    try:
        encrypted_message = encrypt_message(message)
        generate_qr_code(encrypted_message)
        qr_image = tk.PhotoImage(file="/tmp/qr_code.png")
        qr_label.config(image=qr_image)
        qr_label.image = qr_image  # Prevent garbage collection
        logging.info("QR code generated successfully")
    except Exception as e:
        logging.error(f"Failed to generate QR code: {e}")
        messagebox.showerror("Error", "Failed to generate QR code")

# Setup GUI
root = tk.Tk()
root.title("Secure Messenger")
root.geometry("600x400")

tk.Label(root, text="Enter Message (max 256 chars):").pack(pady=5)
message_entry = scrolledtext.ScrolledText(root, height=5, width=60)
message_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=on_generate)
generate_button.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=5)

root.mainloop()

logging.info("Secure Messenger stopped")
