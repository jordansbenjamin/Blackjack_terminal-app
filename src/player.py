##### PLAYER SECTION #####
from calculate import calculate_score
from cards import deal_card

# Initialise empty player hand list, requires this to be global as it is accessed various times throughout the program
player_hand = []

def player_turn():
    '''This function involves logic of players turns and play'''
    
    # Calculates player score from initial dealt cards
    player_score = calculate_score(player_hand)
    # Checks if score is 21, if so players turn automatically ends
    if player_score == 21:
        return
        
    while True: 
        hit_pass = input("Do you want to hit for another card or pass to skip your turn? Type 'h' or 'p': ")

        if hit_pass == 'h':
            print("\n")
            deal_card(1, player_hand)
            # The code below repeats itself because the score has to be re-calculated for conditional statements to check updated score
            player_score = calculate_score(player_hand)
            print(f"Your current hand: {player_hand}, current score: {player_score}")
            if player_score == 21:
                return
            elif player_score > 21:
                return
        elif hit_pass == 'p':
            break
        else:
            print("Please type 'h' to hit for another card or 'p' to pass and skip a turn:\n")