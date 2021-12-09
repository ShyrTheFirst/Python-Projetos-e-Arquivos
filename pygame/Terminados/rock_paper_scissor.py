import random as r

class paper_rock_scissor():
    def __init__(self,player1,player2='Computer'):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
        self.draw_score = 0
        print("Welcome to the paper, rock, scissor game Player %s and %s" %(self.player1,self.player2))
        print('''Each round you have to chose from one of the options:
              Rock, Paper or Scissor.
              Your opponent choose one too.
              Always remember:
              Rock breaks scissor, paper envolve rock, scissor cut paper.
              ''')
    def select_item(self,input1,input2):
        self.choice1 = input1.lower()
        self.choice2 = input2
        self.c1 = ''
        self.c2 = ''
        if self.choice1 == 'r':
            self.c1 = 'r'
        if self.choice1 == 'p':
            self.c1 = 'p'
        if self.choice1 == 's':
            self.c1 = 's'
        if self.choice2 == 1:
            self.c2 = 'r'
        if self.choice2 == 2:
            self.c2 = 'p'
        if self.choice2 == 3:
            self.c2 = 's'

    def define_winner(self):
        if self.c1 == 'r' and self.c2  == 's' or self.c1 == 'p' and self.c2 == 'r' or self.c1 == 's' and self.c2 == 'p':
            print("Gzzz %s you win!" %(self.player1))
            self.player1_score += 1
        if self.c2 == 'r' and self.c1  == 's' or self.c2 == 'p' and self.c1 == 'r' or self.c2 == 's' and self.c1 == 'p':
            print("Oh no! %s win!" %(self.player2))
            self.player2_score += 1
        if self.c2 == 'r' and self.c1  == 'r' or self.c2 == 'p' and self.c1 == 'p' or self.c2 == 's' and self.c1 == 's':
            print("draw")
            self.draw_score += 1

    def endgame(self):
        print("Thanks for playing!\n")
        print(''' Game score:
              %s score is: %i
              %s score is: %i
              number of draws: %i
              ''' %(self.player1,self.player1_score,self.player2,self.player2_score,self.draw_score))
        
            
        


game_loop = True

player1 = input("what's player1 name? ")

game = paper_rock_scissor(player1)

while game_loop:
    player1_choice_define = ''

    input_loop = True
    while input_loop:
        player1_choice = input("player1 : write (R)ock, (P)aper or (S)cissor: ")
        if player1_choice.lower() == 'r' or player1_choice.lower() == 'p' or player1_choice.lower() == 's':
            player1_choice_define = player1_choice
            input_loop = False
        else:
            print("wrong input, try again")
            input_loop = True
            
    player2_choice = r.choice([1,2,3])
    

    game.select_item(player1_choice_define,player2_choice)
    game.define_winner()

    game_loop_continue = input("continue? Y/N ")
    if game_loop_continue.upper() == 'N':
        game_loop = False

game.endgame()




        
        

        
