"""
Christopher Mendez, Rupika Dikkala & Rajesh Mangannavar
Term Project
Blackjack
CS 531 - AI
March 13, 2020
***********************************
"""
import random

class Player:
    def __init__(self, deck):
        self.hand = []
        self.memory = deck
        # balance should also be initialized
        self.balance = 500
        #self.start_bet = 0
        #self.current_bet = 0
        self.current_hand_bet = 0
        # give each player an id..?
        self.id = 0


    def hit(self,deck):
        # pass in card from random card func, for now lets say card = 3
        #card = 3
        #random.randn(13)
        while(1):
            card = random.randint(1, 10)
            if deck[card] > 0:
                deck[card] -= 1
                break
            
            
        
        self.hand.append(card)
        print("current hand: ", self.hand)
        self.memory[card] -= 1
        print("current memory: ", self.memory)


    def reset_hand(self):
        self.hand = []
        
    def initial_bet(self):
        # define minimum bet and pass it in to constructor
        # hardcoding 20 for now
        self.start_bet = 20
        self.current_bet = self.start_bet

    def stand(self):
        pass

    def split(self):
        return

    def double_down(self, deck):
        self.current_bet *= self.current_bet
        self.hit(deck)

        return

    def place_bet(self):
        pass

    # def surrender(self):
    #     if not self.played:
    #         # function to remove player from game
    #         # lose half of start bet
    #         self.start_bet /= 2
    #     else:
    #         print("Sorry, you can't surrender after starting the game")

    def take_action(self, deck, num_decks):
        return


class Dealer(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)

    def take_action(self, deck):
        hand_val = 0
        stand_val = 17
        for x in self.hand:
            hand_val += x
        print("hand value", hand_val)
        if hand_val < stand_val:
            self.hit(deck)
        pass
            
        
        

class DumbAgent(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)

    def take_action(self, deck, num_decks):
        self.hit(deck)
        print("in override take action")

    def place_bet(self, deck, num_decks):
        if self.balance >= 1 :
            self.current_hand_bet = 1
            self.balance -= self.current_hand_bet
        pass


class SmartAgent(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)
        self.runCount = 0
        self.trueCount = 0

    def update_count(self, deck, num_decks):
        num_cards = 0
        self.memory = deck
        for i in range (1, 11):
            if i < 7 and i > 1:
                self.runCount += (4*num_decks - deck[i])
            elif i == 10:
                self.runCount -= (16*num_decks - deck[i])
            elif i == 1:
                self.runCount -= (4*num_decks - deck[i])
            num_cards += deck[i]
        deck_remain = num_cards/52
        self.trueCount = (self.runCount / deck_remain)
        print("Current deck count", self.runCount)
        print("True count", self.trueCount, num_decks)
        print(deck)


    def take_action(self, deck, num_decks):
        self.update_count(deck, num_decks)
        hand_val = sum(self.hand)
        stand_val = 17
        print("hand value", hand_val)
        if hand_val < stand_val:
            self.hit(deck)
        pass
        print("Current deck count in action", self.runCount)
        print("Smart agent making play")

    def place_bet(self, deck, num_decks):
        self.update_count(deck, num_decks)
        betting_unit = 25
        self.current_hand_bet = (self.trueCount * betting_unit)
        if( self.current_hand_bet < betting_unit):
            self.current_hand_bet = betting_unit

        print("I will bet", self.current_hand_bet)
        #make bet


