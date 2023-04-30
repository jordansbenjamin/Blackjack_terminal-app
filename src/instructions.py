from clear import clear_screen

# TODO 3: Create a function that stores information of the games instructions
def instructions():
    clear_screen()
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
    print("\n")

    back = input("Press 'b' to go back to the Main Menu: ")

    match back:
        case 'b':
            clear_screen()