from turtle import *

# from board import *
from board import Board


from turtle import Turtle
import turtle
global cirpos
cirpos=[1,16]
l_valid_pos=[]
l1_pos=[]
l2_pos=[]

scr= turtle.Screen()
global cirmoveflag
cirmoveflag=False
print(id(cirmoveflag))
global cirprevclick
cirprevclick=0
def gam(x,y):
    print(x,y)
    global cirmoveflag
    global cirprevclick
    x1=(x+100)//50
    y1=(100-y)//50
    qud=int(x1+y1*4+1)
    print(qud)
    print('****************************',cirmoveflag)
    if cirmoveflag==True:
        if qud>=17 or qud<=-1:
            print('please choose a position within the board')
            return 0
        print('inside true condition')
        if qud in cirpos:
            print('please choos different position!!')
            cirmoveflag=False
            return 0
        for i in cir:
            print(i.quad)
            print('cirprevclick',cirprevclick)
            if i.quad==cirprevclick:
                print('movcir to be execuited')
                
                cirpos.remove(i.quad)
                i.movcir(qud)
                # print(f'Q= {q}')
                cirmoveflag=False
                print(cirmoveflag)
                print(id(cirmoveflag))
                print('movcir ended')
                print(cirpos)
                print(i.quad)

                cirpos.append(qud)
                print(cirpos)
                return 0

    if qud in cirpos:
        cirmoveflag=True
        print('**************************',cirmoveflag)
        
        cirprevclick=int(qud)
        print('clickprev',cirprevclick)
        

    print(f'x1= {x1}, y1 = {y1}, quad={qud}')
    

class Circles(turtle.Turtle):
    def __init__(self,quad):
        self.cir=turtle.Turtle()
        self.cir.penup()
        self.cir.shape('circle')
        self.cir.shapesize(2)
        x1=(quad-1)%4
        y1=(quad-1)//4
        self.cir.setpos((((2*x1+1)*25)-100,100-(2*y1+1)*25))
        self.quad=int(quad)
    
    def movcir(self,quad):
        x1=(quad-1)%4
        y1=(quad-1)//4
        self.cir.setpos((((2*x1+1)*25)-100,100-(2*y1+1)*25))
        self.quad=int(quad)






c=Circles(1)
c1=Circles(16)
global cir
cir=[c,c1]
# q=int(input('enter quad= '))
# for i in cir:
#     if i.quad==q:
#         i.movcir(5)
#         print(f'Q= {q}')

b=Board()
# b.scrn()
b.draw_board()

button=Board()
button.draw_button(-250,0)
button.draw_button(200,0)
button.draw_button(-250,-100)
button.draw_button(200,-100)



scr.onclick(gam)

mainloop()






















# from turtle import *
# import turtle

# class circles(turtle.Turtle):
#     def __init__(self):
#         self.cir=turtle.Turtle()
#         self.cir.penup()
#         self.cir.setposition(100,100)
#         self.cir.shape('circle')
#         self.cir.shapesize(2)
#         self.quad=0

#     def movcir(self,x,y):
#         print(x,y)
#         x1=(x+100)//50
#         y1=(100-y)//50
#         qud=x1+y1*4+1
#         print("movcir")
#         self.quad=qud
#         self.cir.setpos((((2*x1+1)*25)-100,100-(2*y1+1)*25))
        
        
# def setpo(x,y):
#     x1=(x+100)//50
#     y1=(100-y)//50
#     qud=x1+y1*4+1
#     print(f'x1= {x1}, y1 = {y1}, quad={qud}')
#     return x1,y1,qud

# scr=turtle.Screen()
        
# c=circles()
# # c1=circles()
# global tur
# tur=[c]

# def release(x,y):
#     pass
# circle_pos=[0]
# L1_pos=[[2,6,10,11],[]]

# def game(x,y):
#     a1,b1,q=setpo(x,y)
#     cirmove=False
#     if cirmove==True:
#         pass

#     for i in tur:
#         if q==i.quad:
#             print('before second click')
#     # c.ondrag(c.goto)
            
#             print('function returned')
#             return 0
#             # break
#             # i.quad=
#             # i.cir.setposition(a1,b1)






# scr.onclick(game)
# mainloop()