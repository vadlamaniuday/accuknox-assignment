class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}


rectangle = Rectangle(5, 10)
for area in rectangle:
    print(area)
