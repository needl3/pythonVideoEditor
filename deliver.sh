#!/usr/bin/bash
mkdir ../editor
cp -r ./* ../editor
cd ../editor
sudo rm -r .git test.py note.md .gitignore __pycache__ rendered downloaded_vids venv deliver.sh
cd ../
zip -r editor editor
