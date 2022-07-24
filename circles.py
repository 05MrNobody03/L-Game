from turtle import *

# from board import *
from board import Board


from turtle import Turtle
import turtle
# global cirpos
# cirpos=[1,16]
# l_valid_pos=[]
# l1_pos=[]
# l2_pos=[]

# scr= turtle.Screen()
# global cirmoveflag
# cirmoveflag=False
# print(id(cirmoveflag))
# global cirprevclick
# cirprevclick=0

class Circles(turtle.Turtle):
    Cir=[]
    Cirpos=[1,16]
    def __init__(self,quad):
        self.cir=turtle.Turtle()
        self.cir.penup()
        self.cir.shape('circle')
        self.cir.shapesize(2)
        x1=(quad-1)%4
        y1=(quad-1)//4
        self.cir.setpos((((2*x1+1)*25)-100,100-(2*y1+1)*25))
        self.quad=int(quad)
        self.cirmoveflag=False
        self.cirprevclick=0
        Circles.Cir.append(self)                     #*********************************self.quad
    
    def movcir(self,quad):
        x1=(int(quad)-1)%4
        y1=(int(quad)-1)//4
        self.cir.setpos((((2*x1+1)*25)-100,100-(2*y1+1)*25))
        self.quad=int(quad)
        return 0

        
    def gam(self,qud,prev):
        print(qud)
        print(type(qud))
        cirmoveflag=True
        # cirprevclick=prev
        # print(x,y)
        # global cirmoveflag
        # global cirprevclick
        # x1=(x+100)//50
        # y1=(100-y)//50
        # qud=int(x1+y1*4+1)
        # print(qud)
        print('****************************',cirmoveflag)
        if True:
            # if qud>=17 or qud<=-1:
            #     print('please choose a position within the board')
            #     return 0
            print('inside true condition')
            # if qud in cirpos:
            #     print('please choos different position!!')
            #     self.cirmoveflag=False
            #     return 0
            for i in Circles.Cir:
                print(i.quad)
                print('cirprevclick',prev)
                if i.quad==prev:
                    print('movcir to be execuited')
                    
                    Circles.Cirpos.remove(i.quad)
                    i.movcir(qud)
                    # print(f'Q= {q}')
                    # cirmoveflag=False
                    # print(cirmoveflag)
                    # print(id(cirmoveflag))
                    # print('movcir ended')
                    # print(cirpos)
                    # print(i.quad)

                    Circles.Cirpos.append(qud)
                    print('game returned')
                    # print(cirpos)
                    return 0

