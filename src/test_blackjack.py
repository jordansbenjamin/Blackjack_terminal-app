##### TESTING #####
from pytest import *
from main import *
from calculate import *

# NOTE: Running tests works with the command(pytest -s)

### TEST 1 ###
# CALCULATE SCORE TESTS - This test will assert if the function for calculating the score from the list of cards adds up correctly and returns the sum
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
    # Result: ✅

    # TEST CASE 3: Test player with a hand of six cards and test the return of the sum
    player_hand = ['♣4', '♥2', '♦4', '♠8', '♦2', '♠8']
    # Expected score
    expected_player_score = 28
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Result: ✅

    # TEST CASE 4: Test dealer with natural Blacjack hand (two cards) and returns the sum
    dealer_hand = ['♥A', '♦K']
    # Expected score
    expected_dealer_score = 21
    # Expected Result: Pass
    assert calculate_score(dealer_hand) == expected_dealer_score
    # Result: ✅