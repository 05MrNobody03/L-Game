import turtle
from turtle import Turtle
from turtle import *
from time import *
from time import sleep
scr=turtle.Screen()
# tommy1=turtle.Turtle()
# def box(l,b):
#     for i in range(2):
#         tommy.forward(l)
#         tommy.left(90)
#         tommy.forward(b)
#         tommy.left(90)

# box(50,100)
'''
incorrect l position
l overlapping circle
l overlapping oponents piece
team red won
team blue won

'''

class Popup(turtle.Turtle):
    def __init__(self):
        self.text=turtle.Turtle()
        self.text.penup()
        self.text.hideturtle()
        # self.text.mess=mess
        self.text.text_style = ('Courier', 15, 'bold')
        self.text.x_pos=0
        self.text.y_pos=-220
        self.box=turtle.Turtle()
        self.box.penup()
        self.box.hideturtle()
        # self.box.boxx=box_x
        # self.box.boxy=box_y
        self.box.size=[220,100]
    
    def show_popup(self):
        self.draw_box(-110,-250)
    
    def draw_box(self):
        self.box.penup()
        self.box.setposition(-110,-250)
        self.box.pendown()
        
        for i in range(2):
            self.box.forward(self.box.size[0])
            self.box.left(90)
            self.box.forward(self.box.size[1])
            self.box.left(90)
        self.box.penup()
    def clearbox(self):
        sleep(5)
        self.box.reset()

    def showtext(self,mess):
        self.text.penup()
        self.text.setposition(self.text.x_pos,self.text.y_pos)
        # self.text.pendown()
        self.text.write(mess,font=self.text.text_style,align='center')
        sleep(3)
        self.text.reset()
        self.box.reset()

# tommy.setposition(50,50)
# tommy=Popup()
# # tommy.penup()
# tommy.show_popup()
# # sleep(5)
# tommy.showtext('L overlapping\noponents piece')

# tommy.clearbox()
# # tommy.box.reset()1
# mainloop()