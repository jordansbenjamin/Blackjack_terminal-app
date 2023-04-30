##### TESTING #####
from pytest import *
from main import *
from calculate import *

# NOTE: Running tests works with the command(pytest -s)

# CALCULATE SCORE TESTS
def test_calculate_score():
    # TEST CASE 1: Test player with a hand of two cards and test the sum of their hand
    player_hand = ['♦2', '♠8']
    # Expected score
    player_score = 10
    # Expected Result: Pass
    assert calculate_score(player_hand) == player_score
    # Result: Pass ✅

    # TEST CASE 2: Test dealer with a hand of four cards and test the sum of their hand
    dealer_hand = ['♣6', '♥7']
    # Expected score
    dealer_score = 13
    # Expected Result: Pass
    assert calculate_score(dealer_hand) == dealer_score
    # Result: ✅

    # TEST CASE 3: Test player with a hand of six cards and test the sum of their hand
    player_hand = ['♣4', '♥2', '♦4', '♠8', '♦2', '♠8']
    # Expected score
    player_score = 28
    # Expected Result: Pass
    assert calculate_score(player_hand) == player_score
    # Result: ✅