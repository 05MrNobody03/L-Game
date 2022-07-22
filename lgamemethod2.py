# #possible l positions
# # and basic logic for the game

# global L_pos
# L_pos=[]
# ver=[[1,5,9,10],[2,6,10,9],[2,1,5,9],[2,1,6,10]]
# hor=[[1,2,3,7],[3,7,6,5],[1,5,6,7],[5,1,2,3]]



# def add4andappend(x):
#     global L_pos

#     L_pos.append(x)
#     s=[]
#     for i in range(4):
#         s.append(x[i]+4)
#     L_pos.append(s)
#     print(L_pos)

# # for i in ver:
# #     L_pos.append(i)

# for s in range(3):
    
#     for i in range(4):
#         s1=[]
#         for j in range(4):
#             s1.append(ver[i][j]+s)
#         add4andappend(s1)

# for s in range(3):
    
#     for i in range(4):
#         s1=[]
#         for j in range(4):
#             s1.append(hor[i][j]+s)
#         add4andappend(s1)


# print(len(L_pos))

# for i in L_pos:
#         new_k = []
#         for elem in L_pos:
#             if elem not in new_k:
#                 new_k.append(elem)

# print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
# print(new_k)
# print(len(new_k))

# p= []
# for i in range(48):
#     print(f'{i}sum of  {L_pos[i] } is = {sum(L_pos[i])}')
#     p.append(sum(L_pos[i]))
# print(sorted(p))
# print(len(p))


# # l=[[1,2,3,4],[2,3,4,5],[1,3,4,6],[9,8,7,6],[5,9,8,7],[8,8,7,6],[1,3,5,7],[10,8,7,5],[11,8,7,4]]

# dic={}
# i=0
# while i<len(L_pos):
#     s=sum(L_pos[i])

#     if s in dic:
#         a=dic.get(s)
#         m=a+[L_pos[i]]
#         dic[s]=m
#         i+=1
#     else:
#         dic[s]=[]

# print(dic)
# print(dic.keys())
# l2=list(dic.keys())

# l2=sorted(l2)
# print(l2)






global L_pos
L_pos=[]
hor=[[3,7,6,5]]
def add4andappend(x):
    global L_pos

    L_pos.append(x)
    s=[]
    for i in range(4):
        s.append(x[i]+4)
    L_pos.append(s)
    print(L_pos)

    
for i in range(4):
    s1=[]
    for j in range(4):
        s1.append(hor[i][j]+s)
    add4andappend(s1)
