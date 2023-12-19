#!/bin/bash
cd "$(dirname "$0")"
echo "Hangman Terminal Application Created By Andy Chang"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py