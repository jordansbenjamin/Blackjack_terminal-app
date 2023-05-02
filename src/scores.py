##### CSV SECTION #####
import csv
from prettytable import PrettyTable

game_history = 'game_history.csv'

# TODO 1: Create a function that creates a csv file when one hasn't exist
def create_csv_file():
    '''This function creates the CSV file to store game history and scores.'''
    with open(game_history, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Game', 'Player Hand', 'Dealer Hand', 'Result'])

# TODO 2: Create a function that counts the amount of games played and records that into the CSV
def count_games_played():
    try:
        with open(game_history, 'r') as file:
            reader = csv.reader(file)
            return sum(1 for row in reader)
    except FileNotFoundError:
        return 1

# TODO 4: Create a function that writes the games history to CSV instead of writing it on the play Blackjack function
def write_game_history(player_hand, dealer_hand, winner):
    game_num = count_games_played()
    with open(game_history, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([game_num, player_hand, dealer_hand, winner])

# TODO 3: Create a function that allows the user to read game history from CSV
def view_game_history():
    try:
        with open(game_history, 'r') as file:
            reader = csv.reader(file)
            # header = next(reader)
            # print(f"{' - '.join(header)}")
            next(reader)
            for row in reader:
                print(f"Game {row[0]} - Player Hand: {row[1]}, Dealer Hand: {row[2]}, Result: {row[3]}")
    except FileNotFoundError:
        print("Game history not found")