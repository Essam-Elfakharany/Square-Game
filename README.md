# Square-Game
This is a simple game. There are 8 locations.
each location has some exits shown by arrows.
The player will move from one square to the other one, using the existing exits.
at each move, the player chooses a direction (North, South, East, West) based on the exists available and proposed by the application,
example: the player is at square 7, then the exits are to the direction West and South. 
The player starts at square 1.
The exits are in a dictionary, with the keys being the numbers of the locations(squares) and the values being dictionaries holding the exits (as they do at
present). 
There is no end to the game.
The player keeps moving around the squares.
Once that is working, create another dictionary that contains words(directions) that players may use(North, South, West, East).
These words will be the keys, and their values will be a single letter that the program can use to determine which way to go.
