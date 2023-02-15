# import random

class Players:
    def __init__(self) -> None:
        pass
    
    def player1(self):
        pass

    def player2(self):
        pass

    def player3(self):
        pass

    def player4(self):
        pass

class Cards:
    def __init__(self, random_card) -> None:
        self.random_card1 = random_card

    def hakem(self):
        counter = 0
        for card in self.random_card1:
            counter += 1
            if card == 'ace-heart' or card == 'ace-club' or card == 'ace-diamond' or card == 'ace-spade':
                if counter % 4 == 1:
                    print('hakem is player 1')
                elif counter % 4 == 2:
                    print('hakem is player 2')
                elif counter % 4 == 3:
                    print('hakem is player 3')
                elif counter % 4 == 0:
                    print('hakem is player 4')
                 


a = {
    'ace-heart': 13, 'king-heart': 12, 'queen-heart': 11, 'jack-heart': 10
    }

keys_list = list(a.keys())

random.shuffle(keys_list)
print(keys_list)

a = Cards(keys_list)
a.hakem()