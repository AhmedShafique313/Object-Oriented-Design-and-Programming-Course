class mammal:
    def mammal_info(self):
        print('Mammals can give direct birth')

class Winged_Animals:
    def Winged_info(self):
        print('Winged animals can fly')

class Bat(mammal, Winged_Animals):
    pass

animal1 = Bat()
animal1.mammal_info()
animal1.Winged_info()