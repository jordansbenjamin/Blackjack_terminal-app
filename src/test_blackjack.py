##### TESTING #####
from pytest import *
from main import *
from player import *
from dealer import *
from calculate import *
from winner import *

# NOTE: Running tests works with the command(pytest -s)

### TEST 1 ###
# CALCULATE SCORE FUNCTION 
"""This test will assert if the function for calculating the score from the list of cards adds up correctly and returns the correct sum"""
def test_calculate_score():
    # TEST CASE 1: Test player with a hand of two cards and test the return of the sum
    player_hand = ['♦2', '♠8']
    # Expected score
    expected_player_score = 10
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Result: Pass ✅

    # TEST CASE 2: Test dealer with a hand of four cards and test the return of the sum
    dealer_hand = ['♣5', '♥7', '♠3', '♦4',]
    # Expected score
    expected_dealer_score = 19
    # Expected Result: Pass
    assert calculate_score(dealer_hand) == expected_dealer_score
    # Result: Pass ✅

    # TEST CASE 3: Test player with a hand of six cards and test the return of the sum
    player_hand = ['♣4', '♥2', '♦4', '♠8', '♦2', '♠8']
    # Expected score
    expected_player_score = 28
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Result: Pass ✅

    # TEST CASE 4: Test dealer with natural Blacjack hand (two cards) and returns the sum
    dealer_hand = ['♥A', '♦K']
    # Expected score
    expected_dealer_score = 21
    # Expected Result: Pass
    assert calculate_score(dealer_hand) == expected_dealer_score
    # Result: Pass ✅

### TEST 2 ###
# DETERMINE WINNER FUNCTION
"""This test will assert the correct expected outcome of various winning conditions of the game for both the player and dealer based on the score they have and returns the outcome (win/lose) """
def test_determine_winner():
    # TEST CASE 1: Test the condition when the player recieves a natural Blackjack and returns the correct output
    # Player hand with a natural Blackjack (score of 21)
    player_hand = ['♥A', '♦K']
    # Dealer hand score sums to 10
    dealer_hand = ['♦2', '♠8']
    # Expected outcome: Player wins the game from a natural Blackjack
    expected_output = "Instant win! With a natural Blackjack 🤠"
    # Expected Result: Pass
    assert determine_winner() == expected_output

    # TEST CASE 2: Test the condition when the dealer recieves a natural Blackjack and returns the correct output
    # Dealer hand with a natural Blackjack (score of 21)
    dealer_hand = ['♥A', '♦Q']
    # Player hand score sums to 11
    player_hand = ['♦4', '♠7']
    # Dealer wins the game from a natural Blackjack and Player loses
    expected_output = "You lose! Dealer wins with a natural Blacjack 🤯"
    # Expected Result: Pass
    assert determine_winner() == expected_output

    # TEST CASE 1: Test the condition when the player recieves a natural Blackjack and returns the correct output
    # Player hand with a normal Blackjack (total score of 21)
    player_hand = ['♥7', '♦10', '♠4']
    # Dealer hand score sums to 7
    dealer_hand = ['♦2', '♠5']
    # Expected outcome: Player wins the game from a normal Blackjack
    expected_output = "You won with a Blackjack! 😎"
    # Expected Result: Pass
    assert determine_winner() == expected_output

    # TEST CASE 2: Test the condition when the dealer recieves a natural Blackjack and returns the correct output
    # Dealer hand with a natural Blackjack (score of 21)
    dealer_hand = ['♥A', '♦Q']
    # Player hand score sums to 11
    player_hand = ['♦4', '♠7']
    # Dealer wins the game from a natural Blackjack and Player loses
    expected_output = "You lose! Dealer wins with a Blackjack 😤"
    # Expected Result: Pass
    assert determine_winner() == expected_output