#### CARDS SECTION ####
import numpy as np

# Initialises dictionary of cards
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

# Initialises list of suits
suits = ['♦', '♥', '♠', '♣']

# Initialises empty deck list
deck = []

def init_deck():
    '''This function initialises deck of cards which adds each card to its own respective suits adding up to a total of 52 deck of cards, additionally shuffle the deck of cards'''

    for card in cards_dict:
        for suit in suits:
            cards = suit + card
            deck.append(cards)
    np.random.shuffle(deck)

def draw_card():
    '''This function draws a card from the deck, checks condition if deck of cards is empty then initialise the deck, otherwise pop the card from the deck and return that card'''
    
    if len(deck) == 0:
        init_deck()
    card = deck.pop(0)
    return card

def deal_card(n, hand):
    '''This function adds drawn card for both player and dealer'''
    
    for i in range(n):
        card = draw_card()
        hand.append(card)