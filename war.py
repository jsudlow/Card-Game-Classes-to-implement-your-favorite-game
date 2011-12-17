#!/usr/bin/python
#play a game of war or ANY other game, easily extendable  by Jon Sudlow
#class to implement cards and the shuffling of those cards
import random


class PlayingCard:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    

    #state return methods 
    def show(self):
        print self.rank,"|",self.suit
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def __str__(self):
        return str(self.rank) + str(self.suit)

class Deck:
    def __init__(self,deck):
        self.deck = deck

    def shuffle(self):
        random.shuffle(self.deck,random.random)
    def __str__(self):
        collector = ''
        for object in self.deck:
            out =  object.getRank() + object.getSuit()
            if out == None:
                pass
            else:
                collector += out + " "
                
        return collector
    def take_top_card(self):

        if(len(self.deck) > 0):
            card = self.deck.pop(0)
            return card
        else:
            print 'deck popped off'
    def cards_in_deck(self):
        return len(self.deck)

class Player:
    def __init__(self,name):
        self.hand = []
        self.name = name

    def addCard(self,card):
        self.hand.append(card)

    def removeCard(self):
        return self.hand.pop(0)

    def showHand(self):
        for i in self.hand:
            print i
    def cardsInHand(self):
        return len(self.hand)
class Dealer:
    def __init__(self,name,deck,players):
        self.name = name
        self.deck = deck
        self.players = players
    def deal(self):
        
        while(self.deck.cards_in_deck() != 0):
            top_card = self.deck.take_top_card()
            self.players[0].addCard(top_card)
            next_card = self.deck.take_top_card()

            if next_card is not None:
                self.players[1].addCard(next_card)
  

    def battle(self):
        player1card = self.players[0].removeCard()
        player2card = self.players[1].removeCard()

        rank1 = player1card.getRank()
        rank2 = player2card.getRank()
        print rank1, " vs ",rank2
        if(rank1 > rank2):
            self.players[0].addCard(player1card)
            self.players[0].addCard(player2card)
        else:
            self.players[1].addCard(player1card)
            self.players[1].addCard(player2card)
#add players
jon = Player('Jonathan')
pc = Player('Computer_Opponent')
   
players = [jon,pc]
#define the cards
ac = PlayingCard('11','C')
tend = PlayingCard('10','D')
nineh = PlayingCard('9','H')
eighth = PlayingCard('8','H')
sevenh = PlayingCard('7','H')
sixh = PlayingCard('6','H')



#add the cards to a list
cards_in_deck = [ac,tend,nineh]

#use list to initialize the card deck
playing_deck = Deck(cards_in_deck)

#shuffle the deck
playing_deck.shuffle()
#deal the cards

#add the dealer
dealer = Dealer('Computer_Dealer',playing_deck,players)

#deal the cards out
dealer.deal()

#show hand of jon
print "Jons hand \n"
jon.showHand()

print "Pcs hand \n"
pc.showHand()
print playing_deck



jon.showHand()

print "==============="

pc.showHand()

while(jon.cardsInHand() != 0 and pc.cardsInHand() != 0):
    dealer.battle()


if(jon.cardsInHand() > 0): print "Jonathan WINS!"
else: print "PC WINS :-("
