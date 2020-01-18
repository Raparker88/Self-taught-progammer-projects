class Square:
    square_list=[]
    def __init__(self,s):
        self.side=s
        self.square_list.append(self)
    def __repr__(self):
        print("""{} by {} and {} by {}""".format(self.side,self.side,self.side,self.side))
        
square1=Square(2)
square2=Square(3)
square3=Square(4)

print(square1)
    
