# Blackjack Python Terminal App
---
## Links
#### [GitHub Repo](https://github.com/jordansbenjamin/Blackjack_terminal-app)
#### [Presentation]()
#### [Trello board]()
---
## Installation Guide
#### System Requirements
To play Blackjack, since its a terminal application built on Python. It is a requirement that **Python 3** is installed on your computer.

If you don't have Python 3 already installed, please follow visit this [*website*](https://realpython.com/installing-python/) for steps on installing Python 3 to your device of choice.

Please make sure have **Python 3.11+** version installed.

#### Installation steps (Mac)

1. Open the Mac dedicated terminal by opening **spotlight** with the command:

- **CMD + space**
- Go to the top of menu and look for the **magnifying glass** symbol and click on it.
- Simply type in **'*terminal*'**

2. Once terminal is open, decide where you want the application folder downloaded (like your Desktop for example) like so:
```
cd User/Desktop
```


3. Next, you need to clone the [Github Repo](https://github.com/jordansbenjamin/Blackjack_terminal-app), simply copy and paste this command to your terminal:
```
git clone git@github.com:jordansbenjamin/Blackjack_terminal-app.git
```

4. Next, you need to go to the **src** folder location, type this command on the terminal:
```
cd Blackjack_terminal-app/src
```

5. After that, type these two commands to allow permission for executing the Blackjack program:
```
chmod +x setup_blackjack.sh
chmod +x run_blackjack.sh
```

6. To get you set up before running the Blackjack game program, you need to install some requirements:
```
./setup_blackjack.sh
```

7. After all the necessary requirements are installed, you can now run the program:
```
./run_blackjack.sh
```