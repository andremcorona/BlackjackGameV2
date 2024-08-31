from card import Card

class Hand:
    def __init__(self):
        self.cards = []
        self.aces = 0  # Track aces to adjust for 1 or 11
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value()
        if card.rank == 'A':
            self.aces += 1
        self.adjust_for_aces()

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1