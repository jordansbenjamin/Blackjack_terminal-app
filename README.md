# Blackjack Python Terminal App
## For convenience
#### [GitHub Repo](https://github.com/jordansbenjamin/Blackjack_terminal-app)
#### [Presentation]()
#### [Trello board]()
---
## The Premise

Blackjack fun right on the terminal, the premise is simple, try and get to 21 as close as possible without going over. This application will be a stripped down version of blackjack, with house rules made specifically for this version of the game.

#### House rules

- The deck size is the original 52 cards including suits.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- There are no jokers.
- The deck of cards will be shuffled before starting a game.
- Cards are removed from the deck as they are drawn.
- The dealer is the computer.

---
## Installation Guide
#### System Requirements

To play Blackjack, since its a terminal application built on Python. It is a requirement that **Python 3** is installed on your computer.

If you don't have Python 3 already installed, please follow visit this [*website*](https://realpython.com/installing-python/) for steps on installing Python 3 to your device of choice.

Please make sure have **Python 3.11+** version installed.

Add python version here

#### Installation steps

1. Depending on your operating systems, there are different way to start the installation process:

- For Macintosh `CMD + space` to open spotlight, then simply type in ***terminal***
- For Windows `Windows key + x` then select ***command prompt***

2. Once terminal is open, decide where you want the application folder downloaded (like your Desktop or downloads folder for example) like so:

```
cd User/Desktop
cd User/Downloads
```

3. Next, you need to clone the [Github Repo](https://github.com/jordansbenjamin/Blackjack_terminal-app), simply copy and paste this command to your terminal:

```
git clone https://github.com/jordansbenjamin/Blackjack_terminal-app.git
```

4. Next, you need to go to the **src** folder location, type this command on the terminal:

```
cd Blackjack_terminal-app/src
```

5. After that, type these two commands separately to allow permission for executing the Blackjack program:

```
chmod +x setup_blackjack.sh
```
```
chmod +x run_blackjack.sh
```

6. To get you set up before running the Blackjack game program, you need to install some requirements and dependencies:

```
./setup_blackjack.sh
```

7. After all the necessary requirements are installed, you can now run the program:

```
./run_blackjack.sh
```

8. Enjoy the game! It's important to note when you quit the game, all you need to do to play again is to run the game with the command above. As a reminder: `./run_blackjack.sh`

#### Dependencies

The requirements to start the Blackjack program have the following dependencies, all automatically installed into the virtual envrionment when you follow the steps above:

```
clear==2.0.0
colored==1.4.4
iniconfig==2.0.0
numpy==1.24.3
packaging==23.1
pluggy==1.0.0
prettytable==3.7.0
pytest==7.3.1
wcwidth==0.2.6
```

---
## Features

##### The Player (user)
- Involves logic of how the user interacts and plays the game to win

The player (user) will go against the dealer (computer) for the highest dealt hand up to 21, there are 3 ways the player can win the game:

- If the players hand (cards they recieve) totals to a score of 21, that is a Blackjack and instant win.
- If the players hand total score is higher than the dealers hand, then the player wins.
- If the dealers hand goes over 21, the dealer busts and the player automatically wins the game no matter what card they have.

##### The Dealer (computer)
- Involves logic of how the computer interacts with the game and conditions for it to win

There are 3 ways for the dealer (computer) to win the game:

- If the dealer receives a total card score of 21, that is a blackjack and the player automatically loses. Even if the player has a Blackjack as well.
- If the players total card score is lower than the dealers hand, then the dealer wins.
- If the player overpulls and recieves a total card score over 21, the dealer wins.

However, there is one way for the game to end at a draw:

- At the end of both turns, if the player (user) and dealer (computer) both have the same total card score other than 21, it’s a draw.

##### Main/starting menu

The player will be introduced to the games Menu, just before the game begins, the player has options to do the following:

- The player has the option to start the game instantly, whenever they are ready.
- The option to read instructions.
- The option to read house rules.
- The option to look at the scores of previous games played.

The player will be given the option to go back to the main menu after finishing a game or to continue playing straight away.

---

## Implementation plan

#### Algorithmic thinking

#### Program requirements

#### Flowchart

#### Trello

---
## Code Styling

The Blackjack game was created using Python3, and creating it I followed the conventions and guidelines set by Guido van Rossum, Barry Warsaw and Nick Coghlan with their [PEP 8 - Style Guide For Python Code](https://peps.python.org/pep-0008/).

Code layout conventions such as using 4 spaces of indentation, the consistency of tabs over spaces for indentation. The use of block comments and the use of whitespace in expressions and statements.

Most importantly out of all, the use of descriptive variable and functions names, adding to that I also only used 2 global variables, which follows the convention of having minimal/no global variables.

---
## References