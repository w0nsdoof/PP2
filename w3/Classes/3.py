class point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def show(self):
        print("(" + str(self.x) + " ; " + str(self.y) + ")" ) # (x,y) like math 

    def move(self):
        print("X: ", end= "" )
        self.x = int(input())
        print("Y: ", end= "")
        self.y = int(input())

        return self

    def dist(self):
        return abs(self.x - self.y)


test = point(10, 3)

test.show()

test.move()

test.show()

print(test.dist())



        