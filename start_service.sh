#!/bin/bash

docker build -t yousha_generate_qr_bot .


# Create systemd unit file
cat <<EOF | sudo tee /etc/systemd/system/yousha_generate_qr_bot.service
[Unit]
Description=Yousha Generate QR Bot
Requires=docker.service
After=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker run -p 8080:8080 yousha_generate_qr_bot
ExecStop=/usr/bin/docker stop yousha_generate_qr_bot

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd daemon
sudo systemctl daemon-reload

# Start and enable the service
sudo systemctl start yousha_generate_qr_bot
sudo systemctl enable yousha_generate_qr_bot

# Verify that the service is running
sudo systemctl status yousha_generate_qr_bot
