class animal:
    def super_animal(self):
        print('Cat is a pet and cat is animal')
    
class pet(animal):
    def super_pet(self):
        print('Cat is pet')

class cat(pet):
    def super_cat(self):
        print('Cat')


a1 = cat()
a1.super_animal()
a1.super_pet()
a1.super_cat()