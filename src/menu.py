##### MENU SECTION #####
from colored import fg, bg, attr
from clear import clear_screen
from art import instruction_logo, rules_logo, history_logo
from history import view_game_history, wipe_game_history

def menu():
    '''The menu function displays all the list of menu items for the user to select from'''

    print(f"{attr(1)}{fg(2)}1. Start playing Blackjack{attr('reset')}")
    print(f"{attr(1)}{fg(51)}2. View instructions{attr('reset')}")
    print(f"{attr(1)}{fg(21)}3. View house rules")
    print(f"{attr(1)}{fg(159)}4. Check your game history")
    print(f"{attr(1)}{fg(3)}5. Wipe game history")
    print(f"{attr(1)}{fg(196)}6. Exit Blackjack{attr('reset')}\n")

    # Prompt user for their selection and return selection
    choice = input("Choose a numbered option from the menu: ").strip(' ')
    return choice

def back_to_menu():
    '''A function that allows the user to navigate back to the main menu'''
    
    while True:
        back = input(f"Press {fg(9)}{attr(1)}'b'{attr('reset')} to go back to the Main Menu: ").lower().strip(' ')
        
        try:
            match back:
                    case 'b':
                        clear_screen()
                        return
                    case _:
                        raise ValueError(f"\n{attr(1)}{fg(9)}Invalid Input! Please type 'b':{attr('reset')}\n")
        except ValueError as InvalidInput:
            print(InvalidInput)

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
    '''This function allows the user to decide to wipe and delete the game history, called from the wipe_game_history() function'''

    clear_screen()
    wipe_game_history()
    back_to_menu()
