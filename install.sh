#!/data/data/com.termux/files/usr/bin/bash

pkg update -y
pkg update && pkg upgrade -y
pkg install python -y
pip install -U discord.py
pkg install python git curl -y

rm -rf $HOME/ftj
mkdir -p $HOME/ftj
cd $HOME/ftj

curl -L -O https://raw.githubusercontent.com/boonkongbanpao-sudo/Shoot-the-disc.

chmod +x Shoot-the-disc.
python Shoot-the-disc.
