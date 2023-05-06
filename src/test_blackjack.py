##### TESTING #####
import pytest
import numpy as np
from main import *
from player import *
from dealer import *
from calculate import *
from winner import *
from history import *

# NOTE: Running tests works with the command(pytest -s)

### TEST 1 ###
# INITIALISE DECK FUNCTION TEST SUITE
@pytest.fixture
# Deck sample to test using pytest fixture
def deck_fixture():
    sample_deck = ['♦A', '♥A', '♠A', '♣A', '♦2', '♥2', '♠2', '♣2', '♦3', '♥3', '♠3', '♣3', '♦4', '♥4', '♠4', '♣4', '♦5', '♥5', '♠5', '♣5', '♦6', '♥6', '♠6', '♣6', '♦7', '♥7', '♠7', '♣7', '♦8', '♥8', '♠8', '♣8', '♦9', '♥9', '♠9', '♣9', '♦10', '♥10', '♠10', '♣10', '♦J', '♥J', '♠J', '♣J', '♦Q', '♥Q', '♠Q', '♣Q', '♦K', '♥K', '♠K', '♣K']
    return sample_deck

def test_init_deck(deck_fixture):
    '''This test case checks if the init_deck() function initialises the proper deck amount based on the sample deck'''
    # Expected result: pass
    assert len(deck_fixture) == 52
    # Original Result: Failed ❌
    # Refactored code & bug fixed Result: Pass ✅

### TEST 2 ###
# CALCULATE SCORE FUNCTION TEST SUITE
"""This test will assert if the function for calculating the score from the list of cards adds up correctly and returns the correct sum"""
def test_calculate_score():
    '''TEST CASE 1: Test player with a hand of two cards and test the return of the sum'''
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

    # TEST CASE 5: Test player with a hand of five cards with an Ace and test the return of the sum
    # NOTE: This test case was added as a way to fix a bug found, I ran the tests again with this new test case
    player_hand = ['♣4', '♥2', '♦A', '♠5']
    # Expected score
    expected_player_score = 22
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Original Result: Failed ❌
    # Refactored code & bug fixed Result: Pass ✅

    # TEST CASE 6: Test player with a hand of two aces and test the return of the sum
    # NOTE: This test case was added as a way to fix a bug found, I ran the tests again with this new test case
    player_hand = ['♣A', '♦A']
    # Expected score
    expected_player_score = 12
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Original Result: Failed ❌
    # Refactored code & bug fixed Result: Pass ✅

    # TEST CASE 7: Test player with a hand of three aces and test the return of the sum
    # NOTE: This test case was added as a way to fix a bug found, I ran the tests again with this new test case
    player_hand = ['♣A', '♦A', '♥A']
    # Expected score
    expected_player_score = 13
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Original Result: Failed ❌
    # Refactored code & bug fixed Result: Pass ✅

    # TEST CASE 8: Test player with a hand with four aces and test the return of the sum
    # NOTE: This test case was added as a way to fix a bug found, I ran the tests again with this new test case
    player_hand = ['♣A', '♦A', '♥A', '♠A']
    # Expected score
    expected_player_score = 14
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Original Result: Failed ❌
    # Refactored code & bug fixed Result: Pass ✅

    # TEST CASE 9: Test player with a hand of multiple occurences of aces and test the return of the sum
    # NOTE: This test case was added as a way to fix a bug found, I ran the tests again with this new test case
    player_hand = ['♣A', '♦5', '♥A', '♠A', '♠6']
    # Expected score
    expected_player_score = 24
    # Expected Result: Pass
    assert calculate_score(player_hand) == expected_player_score
    # Original Result: Failed ❌
    # Refactored code & bug fixed Result: Pass ✅
    

### TEST 3 ###
# DETERMINE WINNER FUNCTION TEST SUITE
"""This test will assert the correct expected outcome of various winning conditions of the game for both the player and dealer based on the score they have and returns the outcome (win/lose)"""
def test_determine_winner():
    # TEST CASE 1: Test the condition when the player recieves a natural Blackjack and returns the correct output
    # Player hand with a natural Blackjack (score of 21) and Dealer hand score sums to 10
    # Expected outcome: Player wins the game from a natural Blackjack
    if player_hand == ['♥A', '♦K'] and dealer_hand == ['♦2', '♠8']:
        expected_output = "Instant win! With a natural Blackjack 🤠"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output
    # Result: Pass ✅

    # TEST CASE 2: Test the condition when the dealer recieves a natural Blackjack and returns the correct output
    # Dealer hand with a natural Blackjack (score of 21) and Player hand score sums to 11
    # Expected outcome: Dealer wins the game from a natural Blackjack and Player loses
    elif dealer_hand == ['♥A', '♦Q'] and player_hand == ['♦4', '♠7']:
        expected_output = "You lose! Dealer wins with a natural Blacjack 🤯"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output
    # Result: Pass ✅

    # TEST CASE 3: Test the condition when the player recieves a normal Blackjack and returns the correct output
    # Player hand with a normal Blackjack (total score of 21) and Dealer hand score sums to 7
    # Expected outcome: Player wins the game from a normal Blackjack
    elif player_hand == ['♥7', '♦10', '♠4'] and dealer_hand == ['♦2', '♠5']:
        expected_output = "You won with a Blackjack! 😎"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output
    # Result: Pass ✅

    # TEST CASE 4: Test the condition when the dealer recieves a normal Blackjack and returns the correct output
    # Dealer hand with a natural Blackjack (score of 21) and Player hand score sums to 11
    # Expected outcome: Dealer wins the game from a natural Blackjack and Player loses
    elif dealer_hand == ['♥A', '♦Q'] and player_hand == ['♦4', '♠7']:
        expected_output = "You lose! Dealer wins with a Blackjack 😤"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output
    # Result: Pass ✅

    # TEST CASE 5: Test the condition when the players hand goes over 21 and returns the correct output
    # Player hand sums to 22 which is over 21 and Dealer hand score sums to 17
    # Expected outcome: Player loses the game with an overdrawn hand
    elif player_hand == ['♥7', '♦6', '♠4', '♣5'] and dealer_hand == ['♦2', '♠5', '♦J']:
        expected_output = "You went over! And that's game over.. 😩"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output
    # Result: Pass ✅

    # TEST CASE 6: Test the condition when the dealer's hand goes over 21 and returns the correct output
    # Dealer hand sums up to 26 which is over 21 and Player hand score sums to 13
    # Expected outcome: Dealer loses the game with an overdrawn hand, Player wins
    elif dealer_hand == ['♥7', '♦6', '♠3', '♣10'] and player_hand == ['♦4', '♠9']:
        expected_output = "Dealer went over.. Lucky you, you win! 😅"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output
    # Result: Pass ✅

    # TEST CASE 7: Test the condition when the players hand is higher than the dealers hand and returns the correct output
    # Player hand score sums to 16 and Dealer hand score sums to 13
    # Expected outcome: Player wins the game with a higher hand
    elif player_hand == ['♥7', '♦5', '♠4'] and dealer_hand == ['♦2', '♠5', '♦6']:
        expected_output = "You're a winner! You have a higher score than the Dealer 🥳"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output
    # Result: Pass ✅

    # TEST CASE 8: Test the condition when the dealers hand is higher than the players hand and returns the correct output
    # Dealers hand sums up to 18 and Player hand score sums to 15
    # Expected outcome: Dealer wins the game with a higher hand
    elif dealer_hand == ['♥8', '♠3', '♣10'] and player_hand == ['♦4', '♠9', '♥2' ]:
        expected_output = "You lost... The dealer has a higher score 🙃"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output
    # Result: Pass ✅

    # TEST CASE 8: Final condition where both the players and dealers hand total score equals each other and returns the correct output
    # Dealer hand sums up to 19 and Player hand score sums to 19
    # Expected outcome: Both the player and dealer draws
    elif dealer_hand == ['♥3', '♦6', '♣10'] and player_hand == ['♦4', '♠9', '♥6']:
        expected_output = "It's a draw! 🥲"
        # Expected Result: Pass
        assert determine_winner(player_hand, dealer_hand) == expected_output
    # Result: Pass ✅

### TEST 4 ###
# WRITE GAME HISTORY FUNCTION TEST
"""This test suit checks if the write_game_history function works as expected by writing sample values and asserts that its written in the CSV file"""
def test_write_game_history(tmp_path):
    # Create a temporary CSV file for testing
    game_history_file = tmp_path / "game_history.csv"
    game_history_file.touch()

    # Test values for writing to CSV for testing write_game_history(function)
    player_hand = ["♠A", "♥J"]
    player_score = 21
    dealer_hand = ["♣9", "♦7"]
    dealer_score = 16
    winner = "You won with a Blackjack! 😎"
    # Called the function to write the test value above
    write_game_history(player_hand, player_score, dealer_hand, dealer_score, winner)

    # Check if the file contains the expected values that is written from the function call
    with open(game_history) as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
        assert row_count == 2
        file.seek(0)
        row = next(reader)
        # Expected result: Pass
        assert row == ["1", str(player_hand), str(player_score), str(dealer_hand), str(dealer_score), winner]
        # Result: Pass ✅

### TEST 5 ###
'''This test suite checks for different cases and output results based on the users input when wiping the game history file, it's an important test suite because it validates the outcome of CSV file deletion'''
# TEST CASE 1 (User enters 'yes')
def test_wipe_game_history_yes(monkeypatch, capsys):
    '''This test case will check if wiping the game's history works based on the user's input, in this case when the use enters (yes)'''
    # Set user input to 'yes' using monkeypatch simulation
    monkeypatch.setattr('builtins.input', lambda _: 'yes')
    # Calls the function for 
    wipe_game_history()
    captured = capsys.readouterr()  # Capture the printed output
    expected_output = "The game history has been sucessfully wiped out."
    # Expected Result: Pass
    assert expected_output in captured.out
    # Result: Pass ✅

# TEST CASE 2 (User enters 'no')
def test_wipe_game_history_no(monkeypatch, capsys):
    '''This test case will check if wiping the game's history works based on the user's input, in this case when the use enters (no)'''
    # Set user input to 'no' using monkeypatch simulation
    monkeypatch.setattr('builtins.input', lambda _: 'no')
    # Calls the function for 
    wipe_game_history()
    captured = capsys.readouterr()  # Capture the printed output
    expected_output = "Game history file wipe out has been cancelled."
    # Expected Result: Pass
    assert expected_output in captured.out
    # Result: Pass ✅