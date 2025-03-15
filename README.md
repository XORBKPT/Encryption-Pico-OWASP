
---
# Encryption-Pico-OWASP

**Encryption-Pico-OWASP** is a secure messaging system for research at TuM Institute for Advanced Study, Advanced Computation, Cryptography: Post Doc Bucket: 4. A simple graphical interface, AES-256 encryption, and QR code generation, while staying air-gapped for maximum security. Principles are shown for **ISO/IEC 27001**, **OWASP**, and **NIST**; hence this is in bucket 4 (not "1" <80)
## Overview
This tiny program enables PhD research engineers to:
- **Input Messages**: Enter short messages (up to 256 characters).
- **Encrypt Securely**: Use AES-256-CBC encryption for data protection.
- **Generate QR Codes**: Create scannable QR codes for offline transfer via smartphones in airplane mode.
- **View Easily**: Display QR codes through a glove-friendly interface.
  It demonstrates a few key ideas in a minimal footprint with portability; just a screen, keyboard and Pico:
## Key Features
- **Robust Security**:
  - AES-256-CBC encryption.
  - No hardcoded secrets.
  - Secure key and IV storage.
  - Local audit logging.
- **Intuitive Interface**:
  - Tkinter-based GUI, clickable with gloves for challenging environment (no live graphs included).
- **Dependable QR Codes**:
  - Medium error correction for reliability.
  - Scalable format for future display upgrades.
- **Standards Compliance**:
  - **ISO/IEC 27001**: Audit logging and least privilege.
  - **OWASP**: Input validation.
  - **NIST SP 800-53**: Secure error handling and permissions.
- **Ease of Use**:
  - One-click QR code generation via desktop shortcut.
## Project Files
To deploy Crypto-Zero-QR, you’ll need:
- **`secure_messenger.py`**: Core script for GUI, encryption, and QR code generation.
- **`config.ini`**: Stores user-generated encryption key and IV.
- **`install_dependencies.sh`**: Installs required Python libraries.
- **`setup_autostart.sh`**: Optional script for boot-time autostart.
- **`secure_messenger.desktop`**: Desktop entry for manual launch.
- **`README.md`**: This documentation.
---

## Setup Instructions

### Hardware Requirements
- Raspberry Pi Zero
- MicroSD card (32GB recommended)
- Monitor, keyboard, and mouse
- Optional: Small portable display

### Software Setup
1. **Install Raspberry Pi OS Lite**:
   - Download from the [official site](https://www.raspberrypi.org/software/) and flash it to the microSD card using Raspberry Pi Imager.
   - Insert the card into the Pi Zero and power it on.

2. **Initial Configuration**:
   - Log in with default credentials (`pi` / `raspberry`).
   - Run:
     ```bash
     sudo raspi-config
     ```
   - Update the password.
   - Enable **Desktop Autologin** under **System Options > Boot / Auto Login**.
   - Reboot:
     ```bash
     sudo reboot
     ```

3. **Install Dependencies**:
   - Transfer project files to `/home/pi` (e.g., via USB).
   - Execute:
     ```bash
     chmod +x install_dependencies.sh
     ./install_dependencies.sh
     ```
   - Installs `tkinter`, `qrcode`, `Pillow`, and other dependencies.

4. **Generate Encryption Key and IV**:
   - Create a secure key and IV:
     ```bash
     openssl rand -base64 32  # Key
     openssl rand -base64 16  # IV
     ```
   - Edit `config.ini`:
     ```bash
     nano config.ini
     ```
   - Secure the file:
     ```bash
     chmod 600 config.ini
     ```

5. **Compile to Executable**:
   - Install PyInstaller:
     ```bash
     pip3 install pyinstaller
     ```
   - Compile:
     ```bash
     pyinstaller --onefile secure_messenger.py
     mv dist/secure_messenger secure_messenger.bin
     chmod +x secure_messenger.bin
     ```

6. **Set Up Desktop Shortcut**:
   - Copy to desktop:
     ```bash
     cp secure_messenger.desktop /home/pi/Desktop/
     chmod +x /home/pi/Desktop/secure_messenger.desktop
     ```

7. **Optional Autostart**:
   - Enable autostart:
     ```bash
     chmod +x setup_autostart.sh
     ./setup_autostart.sh
     ```

---

## Usage

1. **Launch the System**:
   - Double-click the **Secure Messenger** desktop icon or run:
     ```bash
     ./secure_messenger.bin
     ```

2. **Enter a Message**:
   - Type a message (max 256 characters) in the text box.

3. **Generate QR Code**:
   - Click **"Generate QR Code"** to encrypt and display the QR code.

4. **Scan the QR Code**:
   - Use a smartphone in airplane mode with a QR scanner to capture it.

5. **Decrypt Later**:
   - Resolve the QR code online (if needed) at lunch, then decrypt at another Pi Zero station.

---

## Security and Compliance

- **ISO/IEC 27001**: Logs audits to `/var/log/secure_messenger.log`, enforces least privilege with the `pi` user.
- **OWASP**: Validates input, avoids hardcoded credentials.
- **NIST SP 800-53**: Ensures secure file permissions and error handling.

---

## Enhancements

- **Advanced QR Codes**: Use higher versions (e.g., `version=2`) or `ERROR_CORRECT_H` for more data or resilience.
- **Styling**: Customize `box_size` or colors in the QR code for better visibility.

---

## Troubleshooting

- **QR Code Not Showing**:
  - Verify `config.ini` has correct key/IV lengths.
- **Errors Occur**:
  - Check `/var/log/secure_messenger.log`.
- **GUI Problems**:
  - Confirm `python3-tk` is installed and **Desktop Autologin** is enabled.

---
