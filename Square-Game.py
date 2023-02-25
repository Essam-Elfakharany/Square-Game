# This is a simple game. There are 8 locations as shown by blue squares. each location has some exits
# shown by arrows. The player will move from one square to the other one, using the existing exits.
# at each move, the player chooses a direction (North, South, East, West) based on the exists available
# and proposed by the application example: the player is at square 7, then the exits are to the direction
# West and South. The player starts at square 1. The exits are in a dictionary, with the keys being the
# numbers of the locations(squares) and the values being dictionaries holding the exits (as they do at
# present). There is no end to the game. The player keeps moving around the squares.
# Once that is working, create another dictionary that contains words(directions) that players may use
# (North, South, West, East). These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.
#########################################Answer################################################
import random as ran
places = {1: "Road", 2: "School", 3: "Building", 4: "Restaurant", 5: "Forest", 6: "Ocean", 7: "Hell", 8: "Paradise"}
directions = {"North": "N", "South": "S", "East": "E", "West": "W"}
exits = {1: {"North": 5, "South": 4, "West": 2, "East": 3},
         2: {"North": 7},
         3: {"West": 1},
         4: {"North": 1, "West": 8, "East": 6},
         5: {"West": 7, "South": 1},
         6: {"West": 4},
         7: {"South": 2, "East": 5},
         8: {"North": 2, "East": 4}}
def printExit(Exit):
    print("Which direction would you like to go:")
    for direction in Exit.keys():
        print(f"[{directions[direction]}]-{direction}")
    print("[Q]-Quit")
def main():
    currentPosition = ran.randint(1, 8)
    print(f"your start position is at location {currentPosition}-{places.get(currentPosition)}")
    while True:
        currentExit = exits.get(currentPosition)
        printExit(currentExit)
        currentDirectionChoices = [directions[direction] for direction in currentExit.keys()]
        currentDirectionChoices.append('Q')
        while (choice := input(
                f"Please enter your choice from {currentDirectionChoices}:").strip().upper()) not in currentDirectionChoices:
            print(f"Error! Invalid input! must choose from {currentDirectionChoices}")
        if choice.strip().upper() == 'Q':
            break
        chosenDirection = list(directions.keys())[list(directions.values()).index(choice.strip().upper())]
        currentPosition = currentExit.get(chosenDirection)
        print(f"Your new position is at location {currentPosition}-{places.get(currentPosition)}")
main()
