##### MENU SECTION #####
from colored import fg, attr
from clear import clear
from art import instruction_logo, rules_logo, history_logo
from history import view_game_history, wipe_game_history

def menu():
    '''The menu function displays all the list of menu items for the user to select from'''

    print(f"{attr(1)}{fg(196)}1. Start playing Blackjack")
    print(f"{attr(1)}{fg(27)}2. Read instructions")
    print(f"{attr(1)}{fg(27)}3. View house rules")
    print(f"{attr(1)}{fg(27)}4. Check game history")
    print(f"{attr(1)}{fg(3)}5. Wipe game history")
    print(f"{attr(1)}{fg(196)}6. Exit Blackjack{attr('reset')}\n")

    # Prompt user for their selection and return selection
    choice = input(f"{attr(1)}Choose a numbered option from the menu: {attr('reset')}").strip(' ')
    return choice

def back_to_menu():
    '''A function that allows the user to navigate back to the main menu'''
    
    while True:
        back = input(f"Press {fg(9)}{attr(1)}'b'{attr('reset')} to go back to the Main Menu: ").lower().strip(' ')
        
        try:
            match back:
                    case 'b':
                        clear()
                        return
                    case _:
                        raise ValueError(f"\n{attr(1)}{fg(9)}Invalid Input! Please type 'b':{attr('reset')}\n")
        except ValueError as InvalidInput:
            print(InvalidInput)

def instructions():
    '''This function allows the user to view the instructions for the game'''

    clear()
    print(instruction_logo)
    
    print(f"""
    The premise of the game is simple, get as close to 21 as possible without going over.
    As the player you will be dealt 2 cards, the dealer will only reveal and present 1 card.
    As the player, you can decide to 'hit' for another card or 'pass' to skip a turn.
    If you get a Natural Blackjack (An Ace and a picture card) you instantly win the game.
    If the dealer gets a Natural Blackjack, you instantly lose the game.
    The game will end if either the players or dealers final hand score is over 21.
    The game will end if either player or dealers final hand score is less than each others.
    You are able to view the game history from the menu to see previous wins/losses.
    You are also able to wipe the game history to start fresh if you wish!
    
    Most importantly have fun, since theres no money involved, no pressure! 😉

    {attr(1)}{fg(9)}NOTE: You can quit the game at any time using the command ctrl + c. Depending on where
          you are in the game, you will either be brought back to the main menu or the game
          will quit.{attr('reset')}
    """)

    back_to_menu()

def rules():
    '''This functions allows the user to view the house rules of the game'''

    clear()
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
    
    clear()
    print(history_logo)
    view_game_history()
    print("\n")
    back_to_menu()

def wipe_history():
    '''This function allows the user to decide to wipe and delete the game history, called from the wipe_game_history() function'''

    clear()
    wipe_game_history()
    back_to_menu()
