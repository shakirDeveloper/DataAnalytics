
from ca_2_car_inventory_system import Car, CarFleet
import random

avaliable_colours = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black" ]
available_makers = [ "toyota", "honda", "suzuki", "bmw", "audi", "kia", "ford", "sokoda" ]
available_models = [ "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013" ]
available_mileage = [ "15", "12", "20", "10", "10", "11", "14", "16" ]

colours = [random.choice(avaliable_colours) for i in range(40)]
makers = [random.choice(available_makers) for i in range(40)]
models = [random.choice(available_models) for i in range(40)]
mileages = [random.choice(available_mileage) for i in range(40)]

cars = []
i=0
for number in range(0, 40):
    car = Car()
    car.setColour(colours[number])
    car.setMake(makers[number])
    car.setMileage(mileages[number])
    car.setModel(models[number])
    cars.append(car)
    print(car.getMake())
    #print(cars[i].getColour())
    i+=1


car_fleet = CarFleet(cars)
car_fleet.mainMenu()
#car_fleet.rentCar(5)
#car_fleet.returnCar(2)
#car_fleet.returnCar(3)




