# cse210-02
# HiLo Game
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
python3 hilo
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hilo folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- hilo               (source code for hilo game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Bob Hathaway (hath22014@byui.edu)

## Design
---
Classes:

Object: card
Responsibility: To hold and display its value
Behaviors: show its value
State: value

Object: deck
Responsibility: 
  To hold 52 cards
Behaviors: 
  Display the next card
  Shuffle
State: a set of 52 shuffled cards

Object: Player
Responsibility: To make a choice about continuing to play and a guess of higher or lower
Behaviors: 
  update score
  display score
  make guess
State:
  score
  guess value
  continuation decision

Object: Dealer
Responsibility: To control the game, get a shuffled deck of cards, show a card, ask the player for their guess of higher and lower,
                    show the next card, determine if the player's score will allow them to continue and ask the player if they want to continue. 
Behaviors: 
State:
  
Class: Dealer
Responsibilities: Director, runs the game, tracking the score and dealing the cards
behaviors: 
  show cards
  show score
  keep score
  ask for inputs



---