class shape:
    class square:
        def __init__(self, length):
            self.length = length

        def area(self):
            return self.length ** 2
            

    class rectangle:
        def __init__(self, length , width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width


object = shape.rectangle(5, 234)

print(object.area())
        



