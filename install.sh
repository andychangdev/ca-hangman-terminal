#!/bin/bash
cd "$(dirname "$0")"
echo "Hangman Terminal Application Created By Andy Chang"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "#!/bin/bash" > hangman.sh
echo "cd '$(dirname "$0")'" >> hangman.sh
echo "source .venv/bin/activate" >> hangman.sh
echo "python main.py" >> hangman.sh
chmod +x hangman.sh
