import turtle
from turtle import *
from turtle import Turtle
from turtle import Screen

from board import Board

color=['blue','red']
brd=Board()
brd.draw_board()
class L_piece(turtle.Turtle):
    def __init__(self):
        self.l=Turtle()
        self.l.penup()
        self.l.pensize(3)
        
    
    def draw_l_piece(self,quad):
        # self.l.pensize(3)
        x1=(quad-1)%4
        y1=(quad-1)//4
        self.l.setpos(((x1*50)-98,98-(y1*50)))
        self.l.color('red')
        self.l.begin_fill()
        for i in range(4):
            self.l.forward(47)
            self.l.right(90)
        self.l.end_fill()
        pass

    def clear_prev_l(self,quad):
        # self.l.pensize(3)
        x1=(quad-1)%4
        y1=(quad-1)//4
        self.l.setpos(((x1*50)-98,98-(y1*50)))
        self.l.color('white')
        self.l.begin_fill()
        for i in range(4):
            self.l.forward(47)
            self.l.right(90)
        self.l.end_fill()
        pass


scr=turtle.Screen()


tommy=L_piece()
# tommy.color('red')
# tommy.pensize(3)
tommy.draw_l_piece(1)
tommy.draw_l_piece(9)
tommy.draw_l_piece(12)
tommy.clear_prev_l(9)
# tommy.begin_fill()
# for i in range(4):
#     tommy.forward(50)
#     tommy.left(90)
# tommy.end_fill()

# turtle.color("black", "red")
# turtle.begin_fill()
# turtle.circle(80)
# turtle.end_fill()
mainloop()