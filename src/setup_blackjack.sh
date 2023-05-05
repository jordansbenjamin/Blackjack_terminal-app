#!/bin/bash

check_python(){
    if ! [[ -x "$(command -v python3)" ]]; then
        echo "Error: 
            To play Blackjack, Python 3 is required and it looks like you don't have it installed.
            Please install Python 3, you can do so by checking out: https://realpython.com/installing-python/" >&2
        exit 1
    fi
}

# Creates virtual environment
create_virtual_venv(){
    python3 -m venv $1
}

# Activates virtual environment
activate_virtual_venv(){
    source $1/bin/activate
}

# Upgrades to the latest version of pip
upgrade_pip(){
    pip install --upgrade pip
}

# Install requirements and dependencies
install_requirements(){
    pip install -r $1  
}

# Main execution of bash script
echo "Welcome! Let's get you setup to play Blackjack!"

check_python

create_virtual_venv blackjack-venv
echo "Virtual environment created!"

activate_virtual_venv blackjack-venv
echo "Virtual environment activated!"

upgrade_pip

clear

install_requirements requirements.txt
echo "Requirements installed!"

clear

echo "Setup complete! Virtual environment initialised, dependencies and requirements installed, to start playing Blackjack, run: ./run_bj.sh"
