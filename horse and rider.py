class Horse():
    def __init__(self,color,rider):
        self.color=color
        self.rider=rider

class Person():

    def __init__(self,name):
        self.name=name

becca=Person("Rebecca Parker")
lola=Horse("tan",becca)
print(lola.rider.name)
