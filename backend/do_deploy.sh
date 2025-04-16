#!/usr/bin/env bash

apt update && apt upgrade -y
apt install -y docker.io git python3-pip

ufw allow 22/tcp
ufw allow 8080/tcp
ufw --force enable

systemctl enable --now docker
usermod -aG docker $USER

git clone https://github.com/your-repo/agentic-deployment.git
cd agentic-deployment

docker build -t agentic . 
docker run -d   --name agentic   -p 8080:8080   -v $PWD/config:/app/config   --restart unless-stopped   agentic

(crontab -l 2>/dev/null; echo "0 3 * * * /usr/bin/docker exec agentic python backup.py") | crontab -
