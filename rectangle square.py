class Shape:
    def __init__(self,w,l):
        self.width=w
        self.length=l
        print("created!")
    def calculate_area(self):
        return self.width*self.length
    def what_am_i(self):
        print("I am a shape")
class Square(Shape):
    pass
    def increase_side(self):
        x=int(input("pick a number: "))
        print("""{} by {}""".format(self.width+x,self.length+x))
class Rectangle(Shape):
    pass


rectangle1=Rectangle(2,3)
rectangle1.what_am_i()

square1=Square(2,2)
square1.what_am_i()
