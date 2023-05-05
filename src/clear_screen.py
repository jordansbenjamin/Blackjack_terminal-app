#### CLEAR FUNCTION ####
from platform import system as system_name
from subprocess import call as system_call

def clear_screen():
    """
    Function to clear terminal screen on windows, linux and mac.
    """
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'

    # Action
    system_call([command])