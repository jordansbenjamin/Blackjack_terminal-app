# Blackjack Python Terminal App

## For convenience

### [GitHub Repo](https://github.com/jordansbenjamin/Blackjack_terminal-app)

### [Presentation](null)

### [Trello board](https://trello.com/b/In1uFmIe/terminal-application-t1a3)

---

## The Premise

Blackjack fun right on the terminal, the premise is simple, try and get to 21 as close as possible without going over. This application will be a stripped down version of blackjack, with house rules made specifically for this version of the game.

### House rules

- The deck size is the original 52 cards including suits.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- There are no jokers.
- The deck of cards will be shuffled before starting a game.
- Cards are removed from the deck as they are drawn.
- The dealer is the computer.
- If the player wins/lose the game before dealer starts their turn, the dealer only reveals one card. Unlike traditional Blackjack, where the dealer reveals their second card at the end of the game.

---

## Installation Guide

### System Requirements

To play Blackjack, since its a terminal application built on Python. It is a requirement that **Python 3** is installed on your computer.

If you don't have Python 3 already installed, please follow visit this [*website*](https://realpython.com/installing-python/) for steps on installing Python 3 to your device of choice.

Please make sure have **Python 3.11+** version installed.

Add python version here

#### Installation steps

1. Depending on your operating systems, there are different way to start the installation process:

- For Macintosh `CMD + space` to open spotlight, then simply type in ***terminal***
- For Windows `Windows key + x` then select ***command prompt***

2. Once terminal is open, decide where you want the application folder downloaded (like your Desktop or downloads folder for example) like so:

```shell
cd User/Desktop
cd User/Downloads
```

3. Next, you need to clone the [Github Repo](https://github.com/jordansbenjamin/Blackjack_terminal-app), simply copy and paste this command to your terminal:

```sehll
git clone https://github.com/jordansbenjamin/Blackjack_terminal-app.git
```

4. Next, you need to go to the **src** folder location, type this command on the terminal:

```shell
cd Blackjack_terminal-app/src
```

5. After that, type these two commands separately to allow permission for executing the Blackjack program:

```shell
chmod +x setup_blackjack.sh
```

```shell
chmod +x run_blackjack.sh
```

6. To get you set up before running the Blackjack game program, you need to install some requirements and dependencies:

```shell
./setup_blackjack.sh
```

7. After all the necessary requirements are installed, you can now run the program:

```shell
./run_blackjack.sh
```

8. Enjoy the game! It's important to note when you quit the game, all you need to do to play again is to run the game with the command above. As a reminder: `./run_blackjack.sh`

#### Dependencies

The requirements to start the Blackjack program have the following dependencies, all automatically installed into the virtual envrionment when you follow the steps above:

```txt
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
#### Main Menu

The player will be introduced to the games Menu, just before the game begins, the player has options to do the following:

- The player has the option to start the game instantly, whenever they are ready.
- The option to read instructions.
    - This will involve a basic overview of the game.
    - Includes option for the user to quit the game at any point using *Ctrl + c*
- The option to read house rules.
    - A quick run down of the games house rules.
- The option to look at the scores of previous games played.
    - This on its own is a feature of the game, which will be explored further down below.
- The option to wipe the game history.
    - Another feature which will be explored below.
- The option to quit the game.
    - User can quit the game from the main menu.

The player will be given the option to go back to the main menu after finishing a game or to continue playing straight away.

#### The Player (user)

This feature involves how the user interacts and plays the game to either win or lose, designing the logic is important as it interacts with various parts of the program. I consider the player as a feature for this reason because it is an important piece of the game but in retrospect its made up of other pieces of the program for it to work properly.

Essentially once the game begins, the player (user) will go against the dealer (computer) for the highest dealt hand up to 21. The player starts their turn first and will be dealt 2 cards to start with, the player then can decide what they want to do as there are 3 ways the player can win the game:

- If the players hand (cards they recieve) totals to a score of 21, that is a Blackjack and instant win.
- If the players hand total score is higher than the dealers hand, then the player wins.
- If the dealers hand goes over 21, the dealer busts and the player automatically wins the game no matter what card they have.

During a round, the player has the option to either:

- *Hit* for another card which is drawn from the deck.
- *Pass* to skip their turn.

Depending on the outcome of their choice for either *hitting* or *passing*, the player will either win or lose. And this can be decided based on the cards they have which involes scores, Throughout the game, the player is able to see their current cards with the respective scores. This in itself is a feature and will be explored in further detail later below.

But essentially, when a player has finished their turn. They will wait for the dealer to make their own decisions which is explored next.

#### The Dealer (computer)

This feature involves all the logic of how the computer interacts with the game and conditions for it to win, with the aim of beating the player. At the start of the game, the dealer will only be dealt one card following rules of traditional Blackjack where only one card is revealed to the player. However, the exception of this games house rule is that if the player wins or loses the game *before* the dealer starts their turn, then the dealer *never* reveals their second card.

This logic is important for the game to work as there are 3 ways for the dealer (computer) to win the game:

- If the dealer receives a total card score of 21, that is a blackjack and the player automatically loses. Even if the player has a Blackjack as well.
- If the players total card score is lower than the dealers hand, then the dealer wins.
- If the player overpulls and recieves a total card score over 21 which is a bust, the dealer wins.

The dealer (computer) decides their turn based on the condition that their card is under 17, they will keep drawing cards while that condition is true and stops if false. This simulates real-life blackjack in a way because the dealer will always want to maximise their winning potential to beat the player.

Once the dealer finishes their turn, it will be revealed who wins/loses the game.

#### Winning conditions, calculating score and the deck of cards

I mentioned earlier that the Player and Dealer features involves other elements (functions) of the program as they provide the logic of turn taking when playing a round of Blackjack based on the conditions who gets to win or lose which involves calculating the scores of both the players and dealers hand.

However, one last condition is that there is one way for the game to end at a draw:

- At the end of both turns, if the player (user) and dealer (computer) both have the same total card score other than 21, it’s a draw.

Again, these conditions are executed based on the score of the players and dealers hand. Calculating the correct sum of the score is important for the game as there is a large number of variability for the outcome of the game based on the cards the player or dealer has.

For example, the house rule that an Ace (which usually has a score of 11) can count as 1 depending on the condition that:

- If the score is over 21 then when an Ace is drawn its counted as 1 instead of 11

This is again important, as it simulates real life Blackjack rules with the exception that tradtionally, the player usually decides if they want to:

- Count Ace as an 11.
- Count Ace as 1.

The deck of cards itself is important, as it deals with the logic of initialising a deck of 52 cards with its respective suits. The deck will be shuffled before the start of every game to maximise the randomness of a game like Blackjack.

More importantly, the logic that involves how a card is drawn from the deck is as important. Where in each of the players and dealers turn they decide if they want to draw another card, if so, then the card is added to their hand and removed from the deck.

#### Game history

This feature involves the use of file handling to keep a tally of the games history based on each round the user plays. For every round:

- The players hand and score is recorded.
- The dealers hand and score is also recorded.
- The result of the games final outcomes is also recorded.
- Finally, the amount of times the game is played is also recorded.

This provides user with the information of past games played so they are able to see how they win or lose, and the user is able to view the game history from the main menu for their convenience.

Not only that, but the user also has the option to wipe the games history and start fresh if they wish to do so. Giving them the flexibility and choice.

Other internal features of the game history feature includes:

- Automatically creates a new file for the user when one hasn't exist yet
- Handles errors that includes:
    - File not found.
    - Permission error.
- When wiping the games history a new one is automatically created for convenience.

#### Other features and functionality

Add this?

There are other smaller pieces that makes up the program as a whole

---

## Implementation plan

#### Planning

To create and design this application, I decided to take roughly just under 1 week as a deadline I set for myself to include all the planning and research that needs to be done for the application. I thought it was important to have this much time with planning and preparation to really flesh out the application before any implementation begins.

For this project, I decided to use Trello for project management which helps me keep track of tasks through the entire process. You can find the [Trello Board here](https://trello.com/b/In1uFmIe/terminal-application-t1a3).

Here is a screenshot of some tasks I laid for the planning phase of the project I added on Trello:

#### Algorithmic thinking

I broke down the programs main requirements into smaller steps to better understand the logic of the game which helps a lot, especially when creating a flowchart which comes up next.

##### Program requirements

1. The user will recieve a starting hand of 2 random cards, but the dealer only gets dealt 1 card as only 1 is revealed.

2. Figure out if the user has a Blackjack which is a picture card like a King, Queen, Jack (value of 10) or a number 10 card, along with an Ace card (value of 11) which equals to total value of 21, this means its a Blackjack and the user automatically wins.

3. Figure out if the dealer (computer) has a Blackjack, if so, the dealer automatically wins.

4. Figure out if both the user and dealer (computer) has a Blackjack, if so, then the dealer wins even though user has a blackjack.

5. Calculate the user’s scores based on the values of their card

6. Calculate the dealer’s (computer) scores based on the values of their card

7. If both the user and dealer (computer) draw an Ace, automatically count this Ace’s value as 11, but if the total of the hand (current cards they have) goes over 21, then the Ace’s value is 1 instead.

8. Only reveal dealers (computer) first card to the user

9. The game will end automatically when the user’s card totals to a score of 21 or if either the user or dealer (computer) gets a Blackjack

10. Prompt the user if they want to draw another card or in the case of Blacjack lingo, another ‘hit’.

11. Prompt the user if they want skip a turn or in the case of Blacjack lingo, a ‘stand’ or ‘standing’.

12. When a user stands and no longer wants to draw a card, they finish their turn and the dealer’s (computer) turn starts. The dealer will keep drawing cards unless their total score goes over 16.

13. Compare users score or dealers (computer) and find out if it’s a win, loss, or draw.

14. Display the users and dealers (computer) final hand along with their scores at the end of the game

15. When the game ends, ask the user if they’d like to play again. Clear the terminal for a fresh slate.

#### Flowchart

I created a flowchart

#### Keeping track of the process using Trello

Trello helped me managed the development process from the planning phase, to testing, development to later polish and make changes to the codebase and all the way creating bash scripts and documentation.

One important takeaway, is that my trello board changed as I added and removed different checklists or due dates, and even changing some parts or features of the application.

So its never set in concrete, and thats great because it shows the process development process is not linear and theres room for flexibility. So unknowingly I applied Agile methodologies during this project.

Again for convenience, please find the [Trello Board here](https://trello.com/b/In1uFmIe/terminal-application-t1a3).

These are screenshots of different cards and sections of my trello board:

---

## Testing

For this application I designed a total of six total test for this application, some I designed early on to implement TDD and some I created during the development process when testing and adding new features.

But most importantly, what I got out of testing was that it helped me discover and fix bugs in the program. Because of the tests I designed, I was able to create new test cases and find that it fails, so I had to refactor my code for the test to pass again. I never thought it would be this helpful.

The tests I designed was to test the outcome of certain functions that had a chance of making a mistake as it involves variability, numerical calculations and conditions.

The tests I designed are:

1. **Initialising deck function test suite**

This test was created to test that the function which initialises the deck of 52 cards sums up correctly, and that it pairs each of the 4 suits to the cards correctly.
- I used a sample deck of cards to assert this function to and turns out I failed the test.
- I found that I was actually missing the card 9 in the cards dictionary!
- So I made those changes and the test passed!

2. **Calculate score function test suite**

This test was designed to check the outcome of the calculate score function, which calculates the score of each cards values and the amount based on either the players or dealers hand.

This was a big and important test as there are many different variabilities and combinations of cards and hands. So I designed up to 9 test cases, 4 of which are originals to the test suite and the other 5 I added as I found potential bugs throughout the development process.

- I created a sample of either players and dealers hand.
- Have the expected score based on that hand.
- Assert that expected score to the calculate score function itself hoping for it to pass.

The errors and bug I found involved the logic that determines the score of an Ace in a card.

For example, when theres 1 Ace in the card

---

## Code Styling

The Blackjack game was created using Python3, and creating it I followed the conventions and guidelines set by Guido van Rossum, Barry Warsaw and Nick Coghlan with their [PEP 8 - Style Guide For Python Code](https://peps.python.org/pep-0008/).

Code layout conventions such as using 4 spaces of indentation, the consistency of tabs (I use tabs instead of spaces which is okay because I consistently use tabs throughout) over spaces for indentation, even though spaces are preferred. The use of block comments and the use of whitespace in expressions and statements.

Most importantly out of all, the use of descriptive variable and functions names, where they're in lowercase with underscores used to separate them. I also used docstrings for all my functions.

Adding to that I also only used 2 global variables, which follows the convention of having minimal/no global variables. Lastly, I group all my imports at the top of the page.

---
## References