#!/data/data/com.termux/files/usr/bin/bash

pkg update -y && pkg install -y python git openssh

git clone https://github.com/your-repo/agentic-deployment.git
cd agentic-deployment

sed -i 's/ENABLE_K8S=.*/ENABLE_K8S=false/g' .env

pip install -r requirements.txt --no-deps

nohup python supervisor.py > agentic.log 2>&1 &

apt install qrencode -y
echo "http://localhost:8080" | qrencode -t ANSIUTF8
