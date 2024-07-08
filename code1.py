class bike:
    name = ""
    price = 0
    gear = 0

bike1 = bike()
bike2 = bike()

bike1.name = "Ducati"
bike1.price = 11000
bike1.gear = 5

bike2.name = "Honda"
bike2.price = 9800
bike2.gear = 5

print(f'Bike name: {bike1.name}, Bike Gears: {bike1.gear}, Bike Price: {bike1.price}')
print(f'Bike name: {bike2.name}, Bike Gears: {bike2.gear}, Bike Price: {bike2.price}')
