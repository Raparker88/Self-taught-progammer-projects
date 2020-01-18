class Hexagon:
    def __init__(var,sl):
        var.side_length=sl
        print("created!")

    def calculate_perimeter(var):
        return var.side_length*6

hexagon1=Hexagon(8)
print(hexagon1.calculate_perimeter())
