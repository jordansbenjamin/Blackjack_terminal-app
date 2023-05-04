#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo "Error: 
        To play Blackjack, Python 3 is required and it looks like you don't have it installed.
        Please install Python 3, you can do so by checking out: https://realpython.com/installing-python/" >&2
    exit 1
fi

if ! [[ -d "blackjack-venv" ]]
then
    echo "Error:
        Virtual environment does not exist, please create a virtual environment by running: ./setup_bj.sh"
fi

if [[ -n "$VIRTUAL_ENV" ]]
then
    clear
    python3 main.py
else
    echo "Vitual environment was not active, activating now..."

    source blackjack/bin/activate
    python3 main.py