import turtle
from turtle import *
from turtle import Turtle
from turtle import Screen

from board import Board

# color=['blue','red']
# brd=Board()
# brd.draw_board()
class L_piece(turtle.Turtle):
    def __init__(self):
        self.l=Turtle()
        self.l.penup()
        self.l.pensize(3)
        self.l.hideturtle()
        self.l.speed(10000)
        
    
    def draw_l_piece(self,quads,col):
        # self.l.pensize(3)
        for quad in quads:
            x1=(int(quad)-1)%4
            y1=(int(quad)-1)//4
            self.l.setpos(((x1*50)-98,98-(y1*50)))
            self.l.color(col)
            self.l.begin_fill()
            for i in range(4):
                self.l.forward(47)
                self.l.right(90)
            self.l.end_fill()
            

    def clear_prev_l(self,quads):
        # self.l.pensize(3)
        for quad in quads:
            x1=(quad-1)%4
            y1=(quad-1)//4
            self.l.setpos(((x1*50)-98,98-(y1*50)))
            self.l.color('cyan')
            self.l.begin_fill()
            for i in range(4):
                self.l.forward(47)
                self.l.right(90)
            self.l.end_fill()
            # pass


# scr=turtle.Screen()


# tommy=L_piece()
# # tommy.color('red')
# # tommy.pensize(3)
# tommy.draw_l_piece(1,'red')
# tommy.draw_l_piece(9,'red')
# tommy.draw_l_piece(12,'red')
# tommy.clear_prev_l(9)
# tommy.begin_fill()
# for i in range(4):
#     tommy.forward(50)
#     tommy.left(90)
# tommy.end_fill()

# turtle.color("black", "red")
# turtle.begin_fill()
# turtle.circle(80)
# turtle.end_fill()
# mainloop()