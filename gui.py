import tkinter as tk
from deck import Deck
from hand import Hand
from utils import *

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        # Create the deck and hands
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

        # Start the first game
        self.start_game()

        # Frame for player and dealer cards
        self.player_frame = tk.Frame(self.root)
        self.player_frame.pack(side=tk.TOP, pady=20)

        self.dealer_frame = tk.Frame(self.root)
        self.dealer_frame.pack(side=tk.TOP, pady=20)

        # Labels to show the player's and dealer's hand values
        self.player_value_label = tk.Label(self.root, text="Player's hand value: ")
        self.player_value_label.pack()

        self.dealer_value_label = tk.Label(self.root, text="Dealer's hand value: ")
        self.dealer_value_label.pack()

        # Buttons for actions (Hit, Stand)
        self.hit_button = tk.Button(self.root, text="Hit", command=self.player_hit)
        self.hit_button.pack(side=tk.LEFT, padx=10)

        self.stand_button = tk.Button(self.root, text="Stand", command=self.player_stand)
        self.stand_button.pack(side=tk.LEFT, padx=10)

        
    
    def start_game(self):
        # Deal a hand
        dealHand(self.deck, self.player_hand, self.dealer_hand)

        # Update the gui to display hand values
        self.update_gui()

    def update_gui(self):
        """Update the display of cards and hand values."""
        # Update player's hand
        self.player_value_label.config(text=f"Player's hand value: {self.player_hand.value}")

        # Update dealer's hand
        self.dealer_value_label.config(text=f"Dealer's hand value: {self.dealer_hand.value}")

    def player_hit(self):
        """Handle player's hit action."""
        self.player_hand.add_card(self.deck.deal())
        self.update_gui()
        if self.player_hand.value > 21:
            self.end_game("You have busted. You lose!")

    def player_stand(self):
        """Handle player's stand action."""
        dealerBust = dealer_turn(self.dealer_hand, self.deck)
        self.update_gui()
        if dealerBust:
            self.end_game("Dealer has busted. You win!")
        elif self.player_hand.value > self.dealer_hand.value:
            self.end_game("You win!")
        elif self.player_hand.value == self.dealer_hand.value:
            self.end_game("It's a push!")
        else:
            self.end_game("Dealer wins!")

    def end_game(self, result):
        """End the game and display the result."""
        tk.messagebox.showinfo("Game Over", result)
        # Ask if the player wants to play again
        play_again = tk.messagebox.askyesno("Play Again", "Do you want to play another hand?")
        if play_again:
            checkForShuffle(self.deck)
            self.start_game()
        else:
            self.root.quit()

