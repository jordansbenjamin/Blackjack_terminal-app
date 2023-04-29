#### CARDS SECTION ####
# from numpy import shuffle
# import random
import numpy as np

# TODO 1: Create dictionary of cards
cards_dict = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

# TODO 2: Create list of suits
suits = ['♦', '♥', '♠', '♣']

# TODO 3: Create empty deck list
deck = []

# TODO 4: Create a function that initialises deck of cards that adds each card to its own respective suits which adds up to a total of 52 deck of cards, additionally shuffle the deck of cards
def init_deck():
    for card in cards_dict:
        for suit in suits:
            cards = suit + card
            deck.append(cards)
    np.random.shuffle(deck)

# init_deck()
# print(deck)

# TODO 5: Create a function that draws a card from the deck, check condition if deck of cards is empty then initialise the deck, otherwise pop the card from the deck and return that card
def draw_card():
    if len(deck) == 0:
        init_deck()
    card = deck.pop(0)
    return card

# u_card = draw_card()
# print(u_card)