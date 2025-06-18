#!/bin/bash

echo "🍩 Donut Terminal Installer"
echo "==========================="

# Update & install dependencies
sudo apt update && sudo apt install -y git curl nodejs npm

git clone https://github.com/unknownmsv/proxy-ai.git
cd proxy-ai

npm install dotenv express axios

node index

