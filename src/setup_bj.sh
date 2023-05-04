#!/bin/bash

echo "Welcome! Let's get you setup to play Blackjack!"

if ! [[ -x "$(command -v python3)"]]
then
    echo "Error: 
        To play Blackjack, Python 3 is required and it looks like you don't have it installed.
        Please install Python 3, you can do so by checking out: https://realpython.com/installing-python/" >&2
    exit 1
fi

# Add echo here
python3 -m venv blackjack-venv

# Add echo here
source blackjack-venv/bin/activate

pip install --upgrade pip

clear

# Add echo here
pip install -r requirements.txt

clear

# Add echo here
echo "Setup complete! Virtual environment initialised, dependencies and requirements installed, to start playing Blackjack, run: ./run_bj.sh"
