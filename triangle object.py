class Triangle:
    def __init__(var,h,b):
        var.height=h
        var.base=b
        print("created!")

    def area(var):
        return (var.height*var.base)/2

triangle1=Triangle(4,6)
print(triangle1.area())
