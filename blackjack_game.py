from deck import Deck
from hand import Hand
from utils import *

def main():
    deck = Deck()
    gameOfBJ(deck)
    
    # Ask user if they would like to keep playing
    playAgain = input("Would you like to play again? (Yes/No): ")

    if playAgain == "Yes":
        checkForShuffle(deck)
        gameOfBJ(deck)


if __name__ == "__main__":
    main()