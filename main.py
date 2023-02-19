import random
from time import sleep

cards_list={
        'ace-heart': 13, 'king-heart': 12, 'queen-heart': 11, 'jack-heart': 10, '10-heart': 9, '9-heart': 8, '8-heart': 7, '7-heart': 6, '6-heart': 5, '5-heart': 4, '4-heart': 3, '3-heart': 2, '2-heart': 1,
        'ace-diamond': 13, 'king-diamond': 12, 'queen-diamond': 11, 'jack-diamond': 10, '10-diamond': 9, '9-diamond': 8, '8-diamond': 7, '7-diamond': 6, '6-diamond': 5, '5-diamond': 4, '4-diamond': 3, '3-diamond': 2, '2-diamond': 1,
        'ace-spade': 13, 'king-spade': 12, 'queen-spade': 11, 'jack-spade': 10, '10-spade': 9, '9-spade': 8, '8-spade': 7, '7-spade': 6, '6-spade': 5, '5-spade': 4, '4-spade': 3, '3-spade': 2, '2-spade': 1,
        'ace-club': 13, 'king-club': 12, 'queen-club': 11, 'jack-club': 10, '10-club': 9, '9-club': 8, '8-club': 7, '7-club': 6, '6-club': 5, '5-club': 4, '4-club': 3, '3-club': 2, '2-club': 1,
        }


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
        self.keys_list = random_card
        self.counter=0


    def hakem(self):
        for card in self.keys_list:
            self.counter += 1
            print(card)
            sleep(1)
            if card == 'ace-heart' or card == 'ace-club' or card == 'ace-diamond' or card == 'ace-spade':
                if self.counter % 4 == 1:
                    print('hakem is player 1')
                    return self.counter
                elif self.counter % 4 == 2:
                    print('hakem is player 2')
                    return self.counter
                elif self.counter % 4 == 3:
                    print('hakem is player 3')
                    return self.counter
                elif self.counter % 4 == 0:
                    print('hakem is player 4')
                    return self.counter
    def hokm(self,cards_list):
        heart = [0,0]
        diamond = [0,0]
        spade = [0,0]
        club = [0,0]
        if self.counter % 4 == 0:
            print(self.keys_list[0:5])
            hokm_is=input("choose a suite : 1.club 2.diamond 3.heart 4.spade\n")
            if hokm_is == '1': hokm_is = 'club'
            elif hokm_is == '2': hokm_is = 'diamond'
            elif hokm_is == '3': hokm_is = 'heart'
            elif hokm_is == '4': hokm_is = 'spade'
            return hokm_is
        else:
            for i in self.keys_list[0:5]:
                if 'heart' in i:
                    heart[0]+=cards_list[i]
                    heart[1]+=1
                elif 'club' in i:
                    club[0]+=cards_list[i]
                    club[1]+=1
                elif 'diamond' in i:
                    diamond[0]+=cards_list[i]
                    diamond[1]+=1
                elif 'spade' in i:
                    spade[0]+=cards_list[i]
                    spade[1]+=1
            listtest3=[]
            listtest2=[('heart',heart[0],heart[1]),('spade',spade[0],spade[1]),('diamond',diamond[0],diamond[1]),('club',club[0],club[1])]
            listtest2.sort(key=lambda a:a[1])
            for i in listtest2:
                if i[1]==(listtest2[3])[1]:
                    listtest3.append(i)
            (listtest3.sort(key=lambda a:a[1]))
            b = listtest3[len(listtest3)-1 ]  
            return b[0]

class run_game:
    
    def __init__(self , keys_list , hakem , hokm) -> None:
        self.hakem = hakem
        self.hokm = hokm
        self.keys_list = keys_list 
        self.Player_cards = [[],[],[],[]]
        
    def run(self):
        counter = 0
        for i in self.keys_list:
            counter += 1
            if counter<=13:
                self.Player_cards[0] .append(i)
            elif counter<=26:
                self.Player_cards[1].append(i)
            elif counter<=39:
                self.Player_cards[2].append(i)
            elif counter<=52:
                self.Player_cards[3].append(i)
    
        # print(self.Player_cards[0])
        # print(self.Player_cards[1])
        # print(self.Player_cards[2])
        # print(self.Player_cards[3])
        return            
                

keys_list = list(cards_list.keys()) 
 
random.shuffle(keys_list)

cards_obj = Cards(keys_list)

hakem = cards_obj.hakem()

random.shuffle(keys_list)

hokm = cards_obj.hokm(cards_list)

run_game_obj = run_game(keys_list,hakem,hokm)
run_game_obj.run()


