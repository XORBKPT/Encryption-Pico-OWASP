#!/bin/bash
echo "[Unit]
Description=Secure Messenger
After=network.target

[Service]
ExecStart=/home/pi/secure_messenger.bin
WorkingDirectory=/home/pi
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/secure_messenger.service
sudo systemctl daemon-reload
sudo systemctl enable secure_messenger.service
