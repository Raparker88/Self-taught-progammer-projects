import math
class Circle:
    def __init__(val,r):
        val.radius=r
        print("created!")

    def area(val):
        return (val.radius*val.radius)*math.pi
circle1=Circle(5)
print(circle1.area())

    
    
