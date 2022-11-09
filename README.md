<h1>The Battleship Destroyer</h1>
  This is a simple game that runs through a terminal provided by the Code Institute on Heroku.
  
  The players may try to beat the game by destroying ships placed at random on a 6 by 6 board.
  
  The deployed project:
  
  <a href="https://dashboard.heroku.com/apps/battle-ship-prtfl3" target="_blank" rel=”noopener”>Battleships</a>
  
![Am I Responsive_ — Mozilla Firefox 01_11_2022 16_51_25 (2)](https://user-images.githubusercontent.com/104979865/199278084-ca674406-80e7-4ddc-9e68-2174745061a2.png)

<h2>How to play</h2>

This is an iteration of a pen-and-paper game Battleships.

In this version of the game a player is greeted with a welcome screen.

After that the player is asked to enter their name.

The game is made up of 6 x 6 grid, and is marked with letters on x axis and numbers on y.

The columns are separated by '|' a symbol.

Players guesses will apear as an O for a missed shot and as an X for a hit.

<h2>Features</h2>

Welcome screen, where a player is asked to push enter in order to move on.

![image](https://user-images.githubusercontent.com/104979865/200787554-8671f19e-bbb5-4163-9d86-18e78f1ce572.png)

A 6 by 6 battle board which holds 7 battle ships randomly placed on it. The goal is to hit at least three boats before the 7 turns run out.

![image](https://user-images.githubusercontent.com/104979865/200787748-56a4ff23-9667-46f6-940a-202501beac97.png)

![image](https://user-images.githubusercontent.com/104979865/200788548-0d9bc866-75f1-4069-8a1a-9f1dd9a4bd91.png)

The game accepts user input which includes numbers form 1 to 6 and letters from a to f. Any other input will be considered invalid.

<h2>Bugs</h2>

A known bug so far is the game not printing out the board after user name input is completed. This does not occur consistently and so far 
I am unaware of how to fix it.

<h2>Testin</h2>

I have manually tested the game and it is in a working state. 

I did run the code through some online validators none of which seemed to point to any problems. 

Though reliability of those validators is questionable.

<h2>Deployment</h2>

This project was deployed using Code Institute's mock terminal for Heroku.

To deploy:
1. Fork or clone a repository
2. Create a new Heroku app
3. Set the buildbacks to Python and NodeJS in that order
4. Link the Heroku app to the repository
5. Click on Deploy

<h2>Credits</h2>

Code Institute for the deployment terminal and the battleship game idea pitch.

This project is a simplified version of this:
<a href="https://github.com/gbrough/battleship/blob/main/5_ship_types_with_computer.py" target="_blank" rel=”noopener”>Game</a>
