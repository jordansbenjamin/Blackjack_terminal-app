##### CSV SECTION #####
import csv

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