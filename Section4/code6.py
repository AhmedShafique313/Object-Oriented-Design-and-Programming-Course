class animal:
    name=""
    def eat(self):
        print('I can drink milk')

class cat(animal):
    def display(self):
        print('My name is ',self.name)


pet1 = cat()
pet1.name="Tom"
pet1.eat()

pet1.display()