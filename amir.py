import random
from time import sleep
from sys import exit


class Cards:
    x=0
    def __init__(self, keys_list) -> None:
        self.keys_list = keys_list
        self.ace_list = ["ace-heart" , "ace-club" , "ace-diamond" , "ace-spade"]
        self.Player_cards = [{'heart':[],'spade':[],'club':[],'diamond':[]},{'heart':[],'spade':[],'club':[],'diamond':[]},{'heart':[],'spade':[],'club':[],'diamond':[]},{'heart':[],'spade':[],'club':[],'diamond':[]}]
        




    def hakem(self):
        for self.x , card in enumerate(self.keys_list):
            self.x = (self.x % 4)+1
            print(f"player{self.x} : {card}")
            sleep(1)
            if card in self.ace_list:
              print(f"hakem is player{self.x}")
              self.x = self.x-1
              return self.x
          
    def hokm(self):
        heart = [0,0]
        diamond = [0,0]
        spade = [0,0]
        club = [0,0]
        if self.x == 0:
            print(self.keys_list[0:5])
            hokm_is=input("choose a suite : 1.club 2.diamond 3.heart 4.spade\n")
            if hokm_is == '1': hokm_is = 'club'
            elif hokm_is == '2': hokm_is = 'diamond'
            elif hokm_is == '3': hokm_is = 'heart'
            elif hokm_is == '4': hokm_is = 'spade'
            else:
                print("Please Enter The Correct Value")
                self.hokm()
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
            list_test=[]
            hakem_hand=[('heart',heart[0],heart[1]),('spade',spade[0],spade[1]),('diamond',diamond[0],diamond[1]),('club',club[0],club[1])]
            hakem_hand.sort(key=lambda a:a[1])
            for i in hakem_hand:
                if i[1]==(hakem_hand[3])[1]:
                    list_test.append(i)
            (list_test.sort(key=lambda a:a[1]))
            hokm= list_test[len(list_test)-1 ]  
            hokm = hokm[0]
            print(hokm )
            return hokm
        
    def playing_cards(self):
        for y , i in enumerate(self.keys_list):
            x = self.x
            y += 1
            if  y <=13:
                if 'heart' in i:
                    self.Player_cards[x]['heart'].append(cards_list[i])
                if 'spade' in i:
                    self.Player_cards[x]['spade'].append(cards_list[i])
                if 'club' in i:
                    self.Player_cards[x]['club'].append(cards_list[i])
                if 'diamond' in i:
                    self.Player_cards[x]['diamond'].append(cards_list[i])
                
            elif y <=26:
                x = (x+1)% 4
                if 'heart' in i:
                    self.Player_cards[x]['heart'].append(cards_list[i])
                if 'spade' in i:
                    self.Player_cards[x]['spade'].append(cards_list[i])
                if 'club' in i:
                    self.Player_cards[x]['club'].append(cards_list[i])
                if 'diamond' in i:
                    self.Player_cards[x]['diamond'].append(cards_list[i])

            elif y <=39:
                x = (x+2)% 4
                if 'heart' in i:
                    self.Player_cards[x]['heart'].append(cards_list[i])
                if 'spade' in i:
                    self.Player_cards[x]['spade'].append(cards_list[i])
                if 'club' in i:
                    self.Player_cards[x]['club'].append(cards_list[i])
                if 'diamond' in i:
                    self.Player_cards[x]['diamond'].append(cards_list[i])

            elif y <=52:
                x = (x+3)% 4
                if 'heart' in i:
                    self.Player_cards[x]['heart'].append(cards_list[i])
                if 'spade' in i:
                    self.Player_cards[x]['spade'].append(cards_list[i])
                if 'club' in i:
                    self.Player_cards[x]['club'].append(cards_list[i])
                if 'diamond' in i:
                    self.Player_cards[x]['diamond'].append(cards_list[i])

        print(self.Player_cards)


class RunGame(Cards):
    def __init__(self):
        self.zamin=[]


    def Start_Game(self,h):
        p=0
        
        if cards_obj.x ==0: 
            print(cards_obj.Player_cards[0])
            first_suit,first_value=input("Enter suit: "),int(input("Enter number: "))
            for i in cards_obj.Player_cards[0][first_suit]:
                if i==first_value:
                    p+=1
                else:
                    pass
            if p==0:
                print("Eshtebahhhh")
            else:
                self.zamin.append(first_suit)
                self.zamin.append(first_value)
                print(self.zamin)
                    
        else:
                min_len = 13
                min_suit = None
                for i in cards_obj.Player_cards[cards_obj.x].keys():
                    if i != h:
                        # print(i)
                        other_suit_list =cards_obj.Player_cards[cards_obj.x][i]
                        if 13 in other_suit_list:
                            min_suit = i
                            min_len = 13
                            break
                        else:
                            other_len = len(other_suit_list)
                            if other_len<min_len:
                                min_len = other_len
                                min_suit = i
                                
                # print(min_len , min_suit)
                # print(min(cards_obj.Player_cards[cards_obj.x][min_suit]))
                self.zamin.append(min_suit)
                self.zamin.append(min_len)
                print(self.zamin)

        


                    
                

            
                 
                 
cards_list={
        'ace-heart': 13, 'king-heart': 12, 'queen-heart': 11, 'jack-heart': 10, '10-heart': 9, '9-heart': 8, '8-heart': 7, '7-heart': 6, '6-heart': 5, '5-heart': 4, '4-heart': 3, '3-heart': 2, '2-heart': 1,
        'ace-diamond': 13, 'king-diamond': 12, 'queen-diamond': 11, 'jack-diamond': 10, '10-diamond': 9, '9-diamond': 8, '8-diamond': 7, '7-diamond': 6, '6-diamond': 5, '5-diamond': 4, '4-diamond': 3, '3-diamond': 2, '2-diamond': 1,
        'ace-spade': 13, 'king-spade': 12, 'queen-spade': 11, 'jack-spade': 10, '10-spade': 9, '9-spade': 8, '8-spade': 7, '7-spade': 6, '6-spade': 5, '5-spade': 4, '4-spade': 3, '3-spade': 2, '2-spade': 1,
        'ace-club': 13, 'king-club': 12, 'queen-club': 11, 'jack-club': 10, '10-club': 9, '9-club': 8, '8-club': 7, '7-club': 6, '6-club': 5, '5-club': 4, '4-club': 3, '3-club': 2, '2-club': 1,
        }
                 
player_list = ['player1', 'player2', 'player3', 'player4']

print("Welcome To Our Game")
sleep(1)
name = input("Please Enter Your Name:")
sleep(1)
print(f"The Name Of This Game is Hokm")
sleep(2)
print(f"{name},You Are Player1")
sleep(2)
print ("Players 1 and 3 are on Team 1. Players 2 and 4 are on Team 2")
sleep(2)
start = input("Are You Ready To Start The Game?( yes / no )\n").lower()
if start == "no" :
    exit()
elif start == "yes":
    print("It's time to deal the cards")
    sleep(1)           
    keys_list = list(cards_list.keys()) 
    
    random.shuffle(keys_list)
    
    cards_obj = Cards(keys_list)
    
    x = cards_obj.hakem()
    
    random.shuffle(keys_list)
    
    h = cards_obj.hokm()
    
    cards_obj.playing_cards()

    p=RunGame()
    p.Start_Game(h)
    
    # run_game_obj = run_game(keys_list,hakem,hokm)
    
    # run_game_obj.playing_cards()


    # runGame_obj = RunGame(player_list, x)
    # runGame_obj.start()