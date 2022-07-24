# here we would have to logic that would take the mouse clicks and do the needful.
## also check for whose turn it is and if the move is valid

from board import Board
from circles import Circles
from L_pieces import L_piece
from L_positions import L_positions

from turtle import Turtle 
from turtle import Screen
import turtle
from turtle import *
from popup import Popup

print('import success')
class Game_logic(turtle.Turtle):

    circle1=Circles(1)
    circle2=Circles(16)
    C=[circle1,circle2]
    brd=Board()
    brd.draw_board()
    
    style = ('Courier', 20, 'bold')
    tommy=turtle.Turtle()
    tommy.penup()
    tommy.setposition(180,100)
    tommy.write('Team Blue', font=style, align='left')
    
    tommy.setposition(-265,100)
    tommy.write('Team Red', font=style, align='left')
    style = ('Courier', 11, 'italic')
    tommy.penup()
    brd.draw_button(-250,0)
    tommy.setposition(-249,7)
    tommy.write('Continue', font=style, align='left')
    
    brd.draw_button(200,0)
    tommy.setposition(201,7)
    tommy.write('Continue', font=style, align='left')
    
    style = ('Courier', 15, 'italic')
    brd.draw_button(-250,-100)
    tommy.setposition(-240,-93)
    tommy.write('Exit', font=style, align='left')
    
    brd.draw_button(200,-100)
    tommy.setposition(210,-93)
    tommy.write('Exit', font=style, align='left')
    print('class objects created')
    L1=L_piece()
    L2=L_piece()
    L_pos=L_positions()
    popup=Popup()
    popup.text.hideturtle()
    popup.box.hideturtle()
    popup.text.penup()
    popup.box.penup()
    popup.text.hideturtle()
    popup.box.hideturtle()
    
    # L1.hideturtle()
    # L2.hideturtle()
    lPiece=[L1,L2]




    def __init__(self):
        print('init done for game logic')
        self.player1_pos=[5,9,10,11]
        self.player1_color='red'
        Game_logic.L1.draw_l_piece(self.player1_pos,self.player1_color)
        self.player1_prevpos=[5,9,10,11]
        self.player2_pos=[6,7,8,12]
        self.player2_color='blue'
        Game_logic.L2.draw_l_piece(self.player2_pos,self.player2_color)
        self.player2_prevpos=[6,7,8,12]
        self.cir12=False
        self.cir12_flag=False
        self.cir_pos=[1,16]
        self.player1_flag=True
        self.player2_flag=False
        self.palyer1_continue=False
        self.player2_continue=False
        self.palyer1_exit=False
        self.player2_exit=False
        self.cir_curr_click=None
        self.cir_prevclick=None
        self.s=[]
        self.count=0
        self.correct=False
        self.chance=1
        # self.



    def whose_chance(self,quad):
        print('inside whose chance')
        print('self.count=',self.count)
        if self.player1_flag==True and self.chance==1:
            print('inside player1')
            if self.count<4:
                print('self.count=',self.count)
            # if tommy.count<4:
                self.s.append(quad)
                # tommy.setposition(x,y)
                # print(tommy.s)
                self.count+=1
                return 0
            else:
                self.s=sorted(self.s)
                self.correct=self.isMoveCorrect1(self.s)
                if self.correct==True:
                    # for i in self.player1_pos:
                    Game_logic.L1.clear_prev_l(self.player1_pos)
                    # for i in self.s:
                    Game_logic.L1.draw_l_piece(self.s,self.player1_color)       #******************************
                    self.player1_pos=self.s
                    self.player1_flag=False
                    self.cir12=True
                    print('player 1 l chance done')
                    
                
                    self.count=0
                    self.s=[]
                    print('self.count=?? ',self.count)
                # print(self.s)
                else:
                    # Game_logic.popup.draw_box()
                    # Game_logic.popup.showtext('L Overlapping\nOther piece')
                    self.count=0
                    self.s=[]

                return 0


        if self.cir12==True:
            print('inside circle')
            if quad in self.cir_pos and self.count==0:
                self.count+=1
                self.cir_prevclick=quad
                self.cir12_flag=True
                return 0
                
            if self.count==1 and self.cir12_flag==True:
                
                self.correct=self.isCirMoveCorrect(quad)
                if self.correct==True:
                    self.count=0
                    
                    for i in Game_logic.C:                                                  # give 2 input to the circle method so that it identifies the cir and moves it to the desired quadrant.
                        self.cir_curr_click=quad
                        if i.quad==self.cir_prevclick:
                            print(f'cur click= {self.currclick}')
                            i.gam(self.cir_curr_click,self.cir_prevclick)
                            print('game returned back')
                    self.cir12=False
                    self.cir_pos.remove(self.cir_prevclick)
                    self.cir_pos.append(self.cir_curr_click)
                    print(self.chance)
                    if self.chance==1:
                        # self.cir12_flag=False
                        self.chance=2
                        print(self.chance)
                        self.player2_flag=True
                        return 0

                    elif self.chance==2:
                        self.player1_flag=True
                        self.chance=1
                        return 0

                    print('out of both')
                    return 0

                    
                else:
                    print('\n\nselect proper quadrant to move circle\n\n')
            



        if self.player2_flag==True and self.chance==2:
            print('inside player2')
            # print('inside player1')
            # if self.count<4:
                        
            # # if tommy.count<4:
            #     self.s.append(quad)
            #     # tommy.setposition(x,y)
            #     # print(tommy.s)
            #     self.count+=1
            #     return 0
            if self.count<=3:
                print('self count= ',self.count)
                        
            
                self.s.append(quad)
                # tommy.setposition(x,y)
                # print(tommy.s)
                self.count+=1
                
                return 0
            else:
                print('inside player2 else')
                self.s=sorted(self.s)
                self.correct=self.isMoveCorrect2(self.s)
                print(self.correct)
                if self.correct==True:
                    # for i in self.player2_pos:
                    print(self.player2_pos)
                    Game_logic.L2.clear_prev_l(self.player2_pos)
                    # for i in self.s:
                    Game_logic.L2.draw_l_piece(self.s,self.player2_color)
                    self.player2_pos=self.s
                    self.player2_flag=False
                    self.cir12=True
                
                self.count=0
                self.s=[]
                # print(self.s)
                return 0
    

    def isCirMoveCorrect(self,quad):
        if quad in self.cir_pos:
            
            Game_logic.popup.draw_box()
            Game_logic.popup.showtext('Select New\nCircle Position')
            return False
        elif quad in self.player1_pos:
            
            Game_logic.popup.draw_box()
            Game_logic.popup.showtext('Circle Overlapping\nL Piece')
            return False
        elif quad in self.player2_pos:
            Game_logic.popup.draw_box()
            Game_logic.popup.showtext('Circle Overlapping\nL Piece')
            return False
        else:
            return True

        

    def isMoveCorrect1(self,s):
        print('inside is move correct1\n')
        print('s=  ',s)
        print(Game_logic.L_pos.L_pos)
        if s in Game_logic.L_pos.L_pos:
            if self.cir_pos[0] in s:
                print('L overlapping with circle')
                    
                Game_logic.popup.draw_box()
                Game_logic.popup.showtext('Circle Overlapping\nL Piece')

                return False
            elif self.cir_pos[1] in s:
                    
                Game_logic.popup.draw_box()
                Game_logic.popup.showtext('Circle Overlapping\nL Piece')
                print('L overlapping with circle')
                return False
            
            for i in self.player2_pos:
                if i in s:
                            
                    Game_logic.popup.draw_box()
                    Game_logic.popup.showtext('Overlapping with\nL Piece')
                    return False
            
            
            print('the s is in L_pos')
            print('self . s = ',s)
            if s != self.player1_pos and s!=self.player2_pos:
                    
                return True
            else:
                Game_logic.popup.draw_box()
                Game_logic.popup.showtext('Overlapping itself\nor Other Piece')
                return False
        else:
            Game_logic.popup.draw_box()
            Game_logic.popup.showtext('Choose Correct\nL Position')
                
            # print('choose correct positions! ')
            # self.count=0

            return False

    
    def isMoveCorrect2(self,s):
        print('inside is move correct\n')
        print('s=  ',s)
        print(Game_logic.L_pos.L_pos)
        if s in Game_logic.L_pos.L_pos:
            if self.cir_pos[0] in s:
                print('L overlapping with circle')
                return False
            elif self.cir_pos[1] in s:
                print('L overlapping with circle')
                return False
            
            for i in self.player1_pos:
                if i in s:
                    return False
            
            
            print('the s is in L_pos')
            print('self . s = ',s)
            if s != self.player1_pos and s!=self.player2_pos:
                return True
            else:
                return False
        else:
            # print('choose correct positions! ')
            # self.count=0

            return False


    def continue1(self):
        self.cir12=False
        self.chance=2
        self.player2_flag=True
        

    def continue2(self):
        self.cir12=False
        self.chance=1
        self.player1_flag=True
        
        pass
    def exit1(self):
        Game_logic.popup.draw_box()
        Game_logic.popup.showtext('Team Blue Won\nTeam Red lost')
                
        print('Player2 Won and Player 1 lost')
        

    def exit2(self):
        Game_logic.popup.draw_box()
        Game_logic.popup.showtext('Player 1 Won\nPlayer 2 lost')
        
        print('Team Red Won and Team Blue lost')
        

    def currclick(self,x,y):
        x1=(x+100)//50
        y1=(100-y)//50
        qud=int(x1+y1*4+1)
        if x>=-250 and x<=-180:
            if y>=0 and y<=35:
                self.continue1()
                return 0
            elif y>=-100 and y<=-65:
                self.exit1()
                return 0
        if x>=200 and x<=270:
            if y>=0 and y<=35:
                self.continue2()
                return 0
            elif y>=-100 and y<=-65:
                self.exit2()
                return 0
        
        
        self.whose_chance(qud)
        print(qud)
        
scr=turtle.Screen()
scr.bgcolor('cyan')
gameON=Game_logic()
print('game lofic completed no lets see clicks')
# scr=turtle.Screen()
# scr.bgcolor('cyan')
scr.onclick(gameON.currclick)
mainloop()

# Brd=Board()
# circle1=Circles()

# import turtle 
# from turtle import *
# from turtle import Screen
# global tommy
# tommy=turtle.Turtle()
# tommy.s=[]
# tommy.count=0
# def posit(x,y):
#     print('inside posit')
    
#     if tommy.count<4:
#         tommy.s.append(x)
#         tommy.setposition(x,y)
#         print(tommy.s)
#         tommy.count+=1
#         return 0
#     else:
#         tommy.count=0
#         tommy.s=[]
#         print(tommy.s)
#         return 0


# scr=Screen()
# scr.onclick(posit)

# mainloop()

