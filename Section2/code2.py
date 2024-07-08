class Rectangle:
    length=0.0
    width=0.0
    def area(self):
        print('Area of Rectangle: ', self.length * self.width)
    
toolbox = Rectangle()

toolbox.length = 10
toolbox.width = 18

toolbox.area()