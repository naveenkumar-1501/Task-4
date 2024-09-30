class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2
    def perimeter(self):
        return 4 * self.side_length
side_lengths = [10, 501, 22, 37, 100, 999, 87, 351]
for side in side_lengths:
    square = Square(side)
    print(f"Side length: {side}")
    print(f"Area: {square.area()}")
    print(f"Perimeter: {square.perimeter()}\n")
