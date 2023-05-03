##### GAME HISTORY CSV SECTION #####
import csv
import os
from prettytable import PrettyTable
from clear import clear_screen

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
        print("Game history file not found")

def wipe_game_history():
    '''This function allows the user to wipe out the game history from the CSV file for a fresh start'''

    choice = input("Are you sure you want to wipe out the game history? This action cannot be undone. Type 'yes' to continue or 'no' to cancel: ").lower().strip(' ')
    print("\n")
    
    try:
        if choice == 'yes':
            try:
                # clear_screen()
                os.remove(game_history)
                print("The game history has been sucessfully wiped out.")
            except FileNotFoundError:
                print("Game history file not found.")
        elif choice.lower() == 'no':
            # clear_screen()
            print("Game history file wipe out has been cancelled.")
    except ValueError:
        print("Invalid input. Please type 'yes' to confirm or 'no' to cancel the wipe out.")
    print("\n")
    return