class L_positions():
    L_pos=[]
    def __init__(self):
        self.h=[[1,2,3,7],[3,5,6,7],[1,5,6,7],[1,2,3,5]]
        self.v=[[1,5,9,10],[2,6,9,10],[1,2,5,9],[1,2,6,10]]
        self.L_pos,self.position_dict,self.sorted_list=self.note_positions(self.h,self.v)
        self.L_pos=[]
        self.note_positions(self.h,self.v)

    def note_positions(self,h,v):
        
        # L_pos=[]        
        for z in range(2):
            for x in range(3):
                for i in range(4):
                    s=[]
                    for j in range(4):
                        s.append(h[i][j]+4*x+1*z)
                    self.L_pos.append(s)


        for z in range(3):
            for x in range(2):
                for i in range(4):
                    s=[]
                    for j in range(4):
                        s.append(v[i][j]+4*x+1*z)
                    self.L_pos.append(s)

        position_dict={}
        i=0
        while i<len(self.L_pos):
            s=sum(self.L_pos[i])

            if s in position_dict:
                a=position_dict.get(s)
                m=a+[self.L_pos[i]]
                position_dict[s]=m
                i+=1
            else:
                position_dict[s]=[]
        
        self.position_dict=position_dict
        sorted_list=list(position_dict.keys())

        self.sorted_list=sorted(sorted_list)
        return self.L_pos,position_dict,sorted_list

        

# L_pos=L_positions()

# print(L_pos.L_pos)
# print(len(L_pos.L_pos))
# print(L_pos.position_dict)
# print(L_pos.sorted_list)
# print(len(L_pos.sorted_list))
