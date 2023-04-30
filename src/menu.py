##### MENU SECTION #####
from clear import clear_screen
from art import instruction_logo

# TODO 1: Create menu function displaying all the list of menu items to select from
def menu():
    print("1. Enter 1 to start playing Blackjack")
    print("2. Enter 2 to view instructions")
    print("3. Enter 3 to view house rules")
    print("4. Enter 4 to check your score history")
    print("5. Enter 5 to exit Blackjack")
    # TODO 2: Prompt user for their selection and return selection
    choice = input("Choose an option from the menu: ")
    return choice

# TODO 3: Create a function that stores information of the games instructions
def instructions():
    clear_screen()
    print(instruction_logo)
    # print("\n")
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
    # print("\n")

    back = input("Press 'b' to go back to the Main Menu: ")

    match back:
        case 'b':
            clear_screen()
            return

# TODO 4: Create a function that stores the house rules of the game