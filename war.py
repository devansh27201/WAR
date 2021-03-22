#card class uses suits,rank, values
import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class Cards:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit
#deck class
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Cards(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
#player class
class player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
player_One = player('One')
player_Two = player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_One.add_cards(new_deck.deal_one())
    player_Two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f'Round{round_num}')
    if len(player_One.all_cards) == 0:
        print('Player One is out of cards! Player Two has won!')
        game_on = False
        break
    if len(player_Two.all_cards) == 0:
        print('Player Two is out of cards! Player One has won!')
        game_on = False
        break
#New Round
    player_One_cards = []
    player_One_cards.append(player_One.remove_one())

    player_Two_cards = []
    player_Two_cards.append(player_Two.remove_one())
    
    at_war = True
    while at_war:
        if player_One_cards[-1].value > player_Two_cards[-1].value:
            player_One.add_cards(player_One_cards)
            player_One.add_cards(player_Two_cards)
            at_war = False
        elif player_One_cards[-1].value < player_Two_cards[-1].value:
            player_Two.add_cards(player_One_cards)
            player_Two.add_cards(player_Two_cards)
            at_war = False
        else:
            print('WAR!!!')
            if len(player_One.all_cards) < 5:
                print('Player One unable to declare war')
                print('Player Two wins the game of WAR!')
                game_on = False
                break
            elif len(player_Two.all_cards) < 5:
                print('Player Two unable to declare war')
                print('Player One wins the game of WAR!')
                game_on = False
                break
            else:
                 for num in range(5):
                    player_One_cards.append(player_One.remove_one())
                    player_Two_cards.append(player_Two.remove_one())