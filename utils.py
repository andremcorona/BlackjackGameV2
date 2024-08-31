from deck import Deck
from hand import Hand

def player_turn(player_hand, dealer_hand, deck):
    while player_hand.value < 22:
        playerChoice = input("\nWould you like to Hit or Stand: ")
        # If user hits
        if playerChoice == "Hit":
            player_hand.add_card(deck.deal())
            print("\nPlayer's hand:", ', '.join(str(card) for card in player_hand.cards))
            print("Player's hand value:", player_hand.value)
            if player_hand.value > 21:
                return True
        # If user stands
        elif playerChoice == "Stand":
            return False
        # Make sure users enter either hit or stand
        else:
            print("\nYou may only enter either Hit or Stand")
    return False

def dealer_turn(dealer_hand, deck):
    # Show dealers entire hand
    print("Dealer's hand:", ', '.join(str(card) for card in dealer_hand.cards))
    print("Dealer's hand value:", dealer_hand.value)

    # Dealer stands on 17 and above
    while dealer_hand.value < 17:  
        dealer_hand.add_card(deck.deal())
        print("")
        print("Dealer's hand:", ', '.join(str(card) for card in dealer_hand.cards))
        print("Dealer's hand value:", dealer_hand.value)
        # Dealer bust on any value above 21
        if dealer_hand.value > 21:
            print("/nDealer has busted.")
            return True
    return False

def checkBJ(hand):
    if hand.value == 21:
        return True
    else:
        return False
    
def dealHand(deck, player_hand, dealer_hand):
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
def checkForShuffle(deck):
    if deck.cards == 0:
        deck.shuffle

def gameOfBJ(deck):
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal initial cards
    dealHand(deck, player_hand, dealer_hand)

    # Show player hands
    print("\nPlayer's hand:", ', '.join(str(card) for card in player_hand.cards))
    print("Player's hand value: ", player_hand.value)
    
    # Show dealer up card
    print("\nDealer's Up card: ", dealer_hand.cards[0])

    # Check for BJ
    playerBJ = checkBJ(player_hand)
    dealerBJ = checkBJ(dealer_hand)

    # Only allow game loop if there is no BJ
    if playerBJ and not dealerBJ:
        print("\nYou have Blackjack! :)")
        gameOn = False
    elif playerBJ and dealerBJ:
        print("Player and Dealer both have Blackjack, it is a push!")
        gameOn = False
    else:
        gameOn = True

    # Game loop starts here
    while gameOn:
        # 1. Players Turn
        playerBust = player_turn(player_hand, dealer_hand, deck)
        if playerBust:
            print("\nYou have busted. You Lose.")
            gameOn = False
        # 2. After players turn and they didn't bust, it is dealers turn
        print("\nNow for the dealer...")
        dealerBust = dealer_turn(dealer_hand, deck)

        # 3. Determine the winner and end the game
        if dealerBust and not playerBust:
            print("\nYou have won! :)")
            gameOn = False
        elif player_hand.value > dealer_hand.value and player_hand.value < 22:
            print("\nYou have won! :)")
            gameOn = False
        elif player_hand.value == dealer_hand.value:
            print("\nIt's a push!")
            gameOn = False
        else:
            print("\nDealer Wins :(")
            gameOn = False