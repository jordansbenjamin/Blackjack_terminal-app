##### GAME HISTORY CSV SECTION #####
import csv
import os
from prettytable import PrettyTable

game_history = 'game_history.csv'

def create_csv_file():
    '''This function creates the CSV file to store game history and scores.'''

    if not os.path.isfile(game_history):
        with open(game_history, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Game', 'Player Hand', 'Player Score', 'Dealer Hand', 'Dealer Score', 'Result'])

def count_games_played():
    '''This function will count the total number of games played by checking the number of rows written in the CSV file'''

    try:
        with open(game_history, 'r') as file:
            reader = csv.reader(file)
            return sum(1 for row in reader)
    except FileNotFoundError:
        return 1

def write_game_history(player_hand, player_score ,dealer_hand, dealer_score ,winner):
    '''This function will write and record the outcome and history of each game played to the CSV file'''

    game_num = count_games_played()
    with open(game_history, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([game_num, player_hand, player_score, dealer_hand, dealer_score, winner])

def view_game_history():
    '''This function will allow the user to view the game history which is recorded and written in the CSV, it also implements prettytable for a better viewing experience'''
    
    try:
        with open(game_history, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            table = PrettyTable(headers)
            for row in reader:
                table.add_row(row)
            print(table)
    except FileNotFoundError:
        print("Game history not found")