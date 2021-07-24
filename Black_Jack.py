import random

#create two lists: suits (hearts,spades, clubs, diamonds), ranks (numbers, jack, queen, king, ace)
suits = ["hearts", "spades", "clubs", "diamonds"]
ranks = ["ten", "nine", "eight", "seven", "six", "five", "four", "three", "two", "jack", "queen", "king", "ace"]
rank_values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 10, 10, 10, 11] #how much each card is worth
values = dict(zip(ranks, rank_values))

playing = True

class Card():
    def __init__(self, suit, rank): #def init takes in the inputs
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self): #def init does not take in the inputs but we still use self
        self.deck = []
        for i in suits:
            for j in ranks:
                self.deck.append(Card(suit = i, rank = j))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n " + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand():
    def __init__(self): #init means initialise
        self.cards = [] #variables we are initiating
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank] #values is the dict - use the key card.rank to access the values rank_values

        if card.rank == "ace":
            self.aces += 1

    def adjust_for_ace(self):
        if self.value >= 21:
            self.value = self.value - (self.aces * 10) #(self.aces * 11) + self.aces
            self.aces -= 1


class Chips():
    def __init__(self, total): #input
        self.total = total #input
        self.bet = 0 #variable we are initiating

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
       self.total = self.total - self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?\n"))
        except:
            print("This is not a number please try again")
        else:
            if chips.bet < chips.total:
                break

def hit(deck, hand): #add the classname
    hand.add_card(deck.deal())  # when calling a function -> classname.function
    hand.adjust_for_ace()


def hit_or_stand(deck,hand): #only applies to the player and not the dealer
    while True:
        playing = True
        try:
            h_s = input("\nDo you want to hit or stand [h/s]?\n")
        except:
            print("\nYou have not imputed [h/s], please try again:\n")
        else:
            if h_s == "h":
                hit(deck, hand)
                return playing
            elif h_s == "s":
                playing = False
                return playing
            else:
                print("You have not imputed [h/s], please try again:\n")

def show_some(player, dealer): #see all if the dealer's cards except for the first one (normal to have a hidden card) but will see all of the player's cards
    print("\nThe player's hand:")
    print(*player.cards, sep="\n") #like f string, * is a special thing ->
    print(f"Value of player's hand: {player.value}")
    print("\nThe dealer's hand:")
    show_dealer_cards = dealer.cards[1:]
    print("<Hidden card>")
    print(*show_dealer_cards, sep="\n")

def show_all(player,dealer):
    print("\nAll the cards in the player's hand:")
    print(*player.cards, sep="\n")
    print("\nAll the cards in the dealer's hand:")
    print(*dealer.cards, sep="\n")

def player_busts(player, dealer, chips): #player points over 21
    print(f"\nYou lost and the dealer won. You have: {player.value} points and the dealer has: {dealer.value} points.")
    chips.lose_bet() #when the player looses we need to deduct the chips from it -> the dealer doesn't have any chips -> also no need to do player.chips.lose_bet() because player is an object formed from the hand and is not in the chip class so it does not have access to the attributes and methods

def player_wins(player, dealer, chips): #player points are higher than the dealer's points
    print(f"\nYou have won and the dealer has lost. You have: {player.value} points and the dealer has: {dealer.value} points.")
    chips.win_bet()

def dealer_busts(player, dealer, chips): #dealer points over 21
    print(f"\nThe dealer has lost and you have won. The dealer has: {dealer.value} points and you have: {player.value} points.")
    chips.win_bet()

def dealer_wins(player, dealer, chips): #dealer points are higher than the player's points
    print(f"\nThe dealer has won and you have lost. The dealer has: {dealer.value} points and you have: {player.value} points")
    chips.lose_bet()

def push(player, dealer):
    print(f"\nIt is a tie. You and the dealer have {player.value} points.")

def replay():
    play_again = input('\nDo you want to play again? [y/n]\n')
    return play_again.lower() == 'y'

while True:

    print("Welcome to Black Jack:\n")

    deck = Deck() #always initialise the object first
    deck.shuffle() #access the properties/methods in that object

    player_hand = Hand()
    player_hand.add_card(deck.deal()) #card = Deck.deal -> where the card is removed and placed into the players hand -> also from now on the deck object should be used instead of the Deck class -> so we see deck.deal() and not Deck.deal() -> as we have made an object for it
    player_hand.add_card(deck.deal())


    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips(500) #use input from init
    take_bet(player_chips) #take_bet is not in the chips class so can't do chips.take_bet -> we have to buse player_chips as an input instead

    show_some(player_hand, dealer_hand)

    while playing: #here the player chooses stand e.g. if number is already big and don't want to risk going over 21
        playing = hit_or_stand(deck, player_hand) #the objects that we have initialised should go in here
        show_some(dealer=dealer_hand, player=player_hand) #the order of inputs is important, but instead of swapping we can just assign the name
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21: #outside the while loop where playing is false
        #the dealer should hit if it's value is less than the player_hand value1 -> this code only runs if the player do not hit

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand) #when the player can't make anymore hits -> the dealer will know -> if dealer's handis higher than the player's -> the dealer auto wins

        show_all(dealer=dealer_hand, player=player_hand)

        if dealer_hand.value > 21:  #check if greater than 21 first if so bust
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

        print(f"You currently have {player_chips.total} chips.\n")

    if not replay():
        print("\nThanks for playing, see you again.\n")
        break



