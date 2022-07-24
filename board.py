# this is for the board of the L game

from turtle import *
import turtle
from pygame import *
import pygame


class Board(turtle.Turtle):

    def __init__(self):
        self.brd=turtle.Turtle()
        self.brd.hideturtle()
        self.brd.pensize(3)
        self.brd.penup()
        self.brd.speed(10000)
    
    # def scrn(self):
    #     self.scr=turtle.Screen()
    #     self.scr.title('L GAME')
    #     self.scr.setup(250,250)

    def draw_board(self):
        
        for j in range(4):
            for i in range(4):
                self.brd.penup()

                self.brd.setposition(-100+50*i,-100+50*j)

                self.draw_square()

        pass

    def draw_square(self):
        self.brd.pendown()
        for i in range(4):
            self.brd.forward(50)
            self.brd.left(90)

        pass

    def draw_button(self,x,y):
        self.brd.penup()
        self.brd.setposition(x,y)
        self.brd.color('yellow')
        self.brd.begin_fill()
        self.brd.pendown()
        self.brd.forward(70)
        self.brd.left(90)
        self.brd.forward(35)
        self.brd.left(90)
        self.brd.forward(70)
        self.brd.left(90)
        self.brd.forward(35)
        self.brd.left(90)
        self.brd.end_fill()
        pass

    def draw_rect(self):
        pass



# # b=Board()
# # # b.scrn()
# # b.draw_board()

# # button=Board()
# # button.draw_button(-250,0)
# # button.draw_button(200,0)
# # button.draw_button(-250,-100)
# # button.draw_button(200,-100)


# mainloop()



# tommy = turtle.Turtle()
# # tommy.hideturtle()
# tommy.pensize(3)
# tommy.speed(10000)
# scr=turtle.Screen()
# scr.title('L GAME')
# scr.setup(250,250)
# # scr.tracer(0,5)

# def draw():
#     tommy.pendown()
#     for i in range(4):
#         tommy.forward(50)
#         tommy. left(90)

# for j in range(4):
#     for i in range(4):
#         tommy.penup()

#         tommy.setposition(-100+50*i,-100+50*j)

#         draw()

# tommy.hideturtle()
# def setpo(x,y):
#     x1=(x+100)//50
#     y1=(100-y)//50
#     qud=x1+y1*4+1
#     print(f'x1= {x1}, y1 = {y1}, quad={qud}')
#     return x1,y1,qud

# # scr.onclick(setpo)

# # scr.onclick(cir)

# global t1
# t1=turtle.Turtle()
# t1.shape('circle')
# t1.shapesize(2)


# global t2
# t2=turtle.Turtle()
# t2.penup()
# t2.shape('circle')
# t2.shapesize(2)
# t2.setposition(100,100)


# def cir(x,y):
#     x1,y1,qud=setpo(x,y)
#     print(f'x1= {x1}, y1 = {y1}, quad={qud}')
#     t1.clearstamps()    
#     # t1=turtle.Turtle()
#     t1.penup()
#     t1.shape('circle')
#     t1.shapesize(2)

#     t1.setpos((((2*x1+1)*25)-100,100-(2*y1+1)*25))
    
#     tommy.penup()
#     # tommy.setpos((((2*x1+1)*25)-100,100-(2*y1+1)*25-20))
    
#     # tommy.pendown()
#     # tommy.color('black')
#     # tommy.fillcolor('black')
#     # tommy.begin_fill()
#     # tommy.circle(20)
#     # tommy.end_fill
#     # # tommy.fillcolor('black')
#     # tommy.showturtle()
#     # pass


# # buttons
# def buttons(x,y):
#     tommy.penup()
#     tommy.setposition(x,y)
#     tommy.pendown()
#     tommy.forward(70)
#     tommy.left(90)
    
#     tommy.forward(35)
#     tommy.left(90)
#     tommy.forward(70)
#     tommy.left(90)
#     tommy.forward(35)
#     tommy.left(90)


# buttons(-200,0)
# buttons(200,0)
# buttons(-200,-100)
# buttons(200,-100)


# def game(x,y):
    
#     pass

# scr.onclick(cir)
#***************************************************************************
# def squ():
#     tommy.pendown()
#     for i in range(4):
#         tommy.forward(50)
#         tommy. left(90)


# for i in range(3):
#     tommy.penup()
#     tommy.setposition(0,50*i)
#     squ()

# tommy.penup()
# tommy.setposition(50,0)   
# squ() 

# scr.addshape('circle.gif')
# tommy.shape('circle.gif')

# tommy.setposition(0,200)
# player = pygame.image.load('circle12.png')    #.convert()


# Draw rectangle around the image
# rct = player.get_rect()
# rct.center = 50,50





# Set moving and running values
# rnnng = True
# mvng = False

# Setting what happens when the game
# changes to running state
# while rnnng:

#     for vnt in pygame.event.get():

# # Close the app if user wants it
#         if vnt.type == QUIT:
#             rnnng = False



# # Moving the image
#         elif vnt.type == MOUSEBUTTONDOWN:
#             if rct.collidepoint(vnt.pos):
#                 mvng = True

#         # If you want to move the picture with a mouse click, set # to False. If you want to move the picture without using the #mouse, set moving to True.
#         elif vnt.type == MOUSEBUTTONUP:
#             mvng = False

#         # Make your image move continuously
#         elif vnt.type == MOUSEMOTION and mvng:
#             rct.move_ip(vnt.rel)










# scr.update() #********************************************************
#***********************************************************************





# # Move the image with the mouse with a Python program

# # Importing the library pygame
# import pygame
# from pygame.locals import *

# #Consider your color choices.
# YELLOW = (255, 255, 0)
# BLUE = (0, 0, 255)

# # Create the user interface for the game.
# pygame.init()

# # Set the size of the game's user interface.
# wi, hi = 640, 350
# scrn = pygame.display.set_mode((wi, hi))

# # Take image as input
# imge = pygame.image.load('circle12.png')
# imge.convert()

# # Draw rectangle around the image
# rct = imge.get_rect()
# rct.center = wi//2, hi//2

# # Set moving and running values
# rnnng = True
# mvng = False

# # Setting what happens when the game
# # changes to running state
# while rnnng:

#     for vnt in pygame.event.get():

# # Close the app if user wants it
#         if vnt.type == QUIT:
#             rnnng = False

# # Moving the image
#         elif vnt.type == MOUSEBUTTONDOWN:
#             if rct.collidepoint(vnt.pos):
#                 mvng = True

# # If you want to move the picture with a mouse click, set # to False. If you want to move the picture without using the #mouse, set moving to True.
#         elif vnt.type == MOUSEBUTTONUP:
#             mvng = False

# # Make your image move continuously
#         elif vnt.type == MOUSEMOTION and mvng:
#             rct.move_ip(vnt.rel)

# # Set image on screen and color
# scrn.fill(YELLOW)
# scrn.blit(imge, rct)

# # Construct the image's border
# pygame.draw.rect(scrn, BLUE, rct, 2)

# # save the new changes in GUI pygame
# pygame.display.update()
# print('hello world')
# # Quit the GUI game
# pygame.quit()