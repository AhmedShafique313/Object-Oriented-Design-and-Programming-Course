class car:
    name = ''
    model = ''
    price = 0

car1 = car()

car1.name = input('Enter car name: ')
car1.model = input(f'Enter the model name of {car1.name}: ')
car1.price = input(f'Enter the price name of {car1.name} {car1.model}: ')
print(f'I hava an {car1.name} {car1.model} and its price is {car1.price} Dollars in USA')