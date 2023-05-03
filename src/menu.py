##### MENU SECTION #####
from clear import clear_screen
from art import instruction_logo, rules_logo, history_logo
from history import view_game_history, wipe_game_history

def menu():
    '''The menu function displays all the list of menu items for the user to select from'''

    print("1. Enter 1 to start playing Blackjack")
    print("2. Enter 2 to view instructions")
    print("3. Enter 3 to view house rules")
    print("4. Enter 4 to check your game history")
    print("5. Enter 5 to wipe game history")
    print("6. Enter 6 to exit Blackjack")

    # Prompt user for their selection and return selection
    choice = input("Choose an option from the menu: ")
    return choice

def back_to_menu():
    '''A function that allows the user to navigate back to the main menu'''
    
    while True:
        back = input("Press 'b' to go back to the Main Menu: ")
        
        match back:
            case 'b':
                clear_screen()
                return
            case _:
                # clear_screen()
                print("Please type 'b': ")

def instructions():
    '''This function allows the user to view the instructions for the game'''

    clear_screen()
    print(instruction_logo)
    
    print("""
    The premise of the game is simple, get as close to 21 as possible without going over.
    As the player you will be dealt 2 cards, the dealer will also have 2 cards.
    However, the dealer will only present one of its card.
    As the player, you can decide to 'hit' for another card or 'pass' to skip a turn.
    If you get a Natural Blackjack (An Ace and a picture card) you instantly win the game.
    If the dealer gets a Natural Blackjack, you instantly lose the game.
    The game will end if either the players or dealers final hand score is over 21.
    The game will end if either player or dealers final hand score is less than each others.
    """)

    back_to_menu()

def rules():
    '''This functions allows the user to view the house rules of the game'''

    clear_screen()
    print(rules_logo)
    print("""
    The deck size is the original 52 cards including suits.
    The Jack/Queen/King all count as 10.
    The Ace can count as 11 or 1.
    There are no jokers.
    The deck of cards will be shuffled before starting a game.
    Cards are removed from the deck as they are drawn.
    The dealer is the computer.
    """)

    back_to_menu()
        
def history():
    '''This functions allows the user to view the history and score of games played, called from view_game_history() function'''
    
    clear_screen()
    print(history_logo)
    view_game_history()
    print("\n")
    back_to_menu()

def wipe_history():
    '''This function allows the user to decide to wipe and delete the game history'''

    clear_screen()
    # Print wipe logo here
    wipe_game_history()
    print("\n")
    back_to_menu()
    