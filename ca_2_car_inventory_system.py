# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:42:01 2020

@author: MyFirstLaptop
"""

class Car(object):
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__model = ''
        self.__mileage = 0
        self.__type = ''
        
    def setType(self, type):
        self.__type = type
        
    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setMileage(self, mileage):
        self.__mileage = mileage

    def getMileage(self):
        return self.__mileage
    
    def __str__(self):
        return '"{0}","{1}","{2}","{3}","{4}"\n'.format(
        self.__colour, self.__make,
        self.__model, self.__mileage, self.__type)


class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells
    def __str__(self):
        return '"{0}","{1}","{2}","{3}","{4}","{5}"\n'.format(
            self.__colour, self.__make,
            self.__model, self.__mileage,
            self.__numberFuelCells, 'Electric' )
        
class HybridCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        self.__engineSize = 660
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells
    
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize
    def __str__(self):
        return '"{0}","{1}","{2}","{3}","{4}","{5}"\n'.format(
            self.__colour, self.__make,
            self.__model, self.__mileage,
            self.__engineSize, 'Hybrid' )

class PetrolCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = 660
        
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize
    def __str__(self):
        return '"{0}","{1}","{2}","{3}","{4}","{5}"\n'.format(
            self.__colour, self.__make,
            self.__model, self.__mileage,
            self.__numberFuelCells, 'Petrol' )

class DieselCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = 1000
        
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize
    def __str__(self):
        return '"{0}","{1}","{2}","{3}","{4}","{5}"\n'.format(
            self.__colour, self.__make,
            self.__model, self.__mileage,
            self.__numberFuelCells, 'Diesel' )

class CarFleet():
    
    def __init__(self,cars):
        self.__pathOfWriteData = 'C:\\BD_CA_2_Output.csv'
        self.__petrol_cars = []
        self.__electric_cars = []
        self.__diesel_cars = []
        self.__hybrid_cars = []
        self.__rented_cars=[]
        for i in range(0, 20):
            cars[i].setType("Petrol")
            self.__petrol_cars.append(cars[i])            
        for i in range(20, 26):
            cars[i].setType("Electric")
            self.__electric_cars.append(cars[i])
        for i in range(26, 36):
            cars[i].setType("Diesel")
            self.__diesel_cars.append(cars[i])
        for i in range(36, 40):
            cars[i].setType("Hybrid")
            self.__hybrid_cars.append(cars[i])
        
    def getPetrolCars(self):
        return self.__petrol_cars
    def getElectricCars(self):
        return self.__electric_cars
    def getDieselCars(self):
        return self.__diesel_cars
    def getHybridCars(self):
        return self.__hybrid_cars

    def checkCarsInStock(self):
        print('Number of Petrol Cars : ' + str(len(self.getPetrolCars())))
        print('Number of Electric Cars : ' + str(len(self.getElectricCars())))
        print('Number of Diesel Cars : ' + str(len(self.getDieselCars())))
        print('Number of Hybrid Cars : ' + str(len(self.getHybridCars())))
        
    def checkDesireCarInStock(self, type, quantity):        
        if type == 'P':
            if len(self.getPetrolCars()) < quantity:
                print("Petrol car is not available in desire quantity")
                return 0
        elif type == 'E':
            if len(self.getElectricCars()) < quantity:
                print("Electric car is not available in desire quantity")
                return 0
        elif type == 'D':
            if len(self.getDieselCars()) < quantity:
                print("Diesel car is not available in desire quantity")
                return 0
        elif type == 'H':
            if len(self.getHybridCars()) < quantity:
                print("Hybrid car is not available in desire quantity")
                return 0
        return 1
        #return "your selected car type is not in stock"
    
    def save_csv(self,commits):
        #print(commits)
        csv_file = open(self.__pathOfWriteData, 'w')
        csv_file.write('Number of Petrol cars : {0}\n'.format(len(self.getPetrolCars())))
        csv_file.write('Number of Diesel cars : {0}\n'.format(len(self.getDieselCars())))
        csv_file.write('Number of Electric cars : {0}\n'.format(len(self.getElectricCars())))
        csv_file.write('Number of Hybrid cars : {0}\n'.format(len(self.getHybridCars())))
        csv_file.write('Colour,Maker,Model,Mileage,Type\n')
        for commit in commits:        
            csv_file.write(str(commit))
       
        csv_file.close()
        
    def get_all_cars_list(self):        
        all_cars_list = []
        all_cars_list.extend(self.__petrol_cars)
        all_cars_list.extend(self.__electric_cars)
        all_cars_list.extend(self.__diesel_cars)
        all_cars_list.extend(self.__hybrid_cars)        
        return all_cars_list
    

    def rent(self, type, quantity):        
        if type == 'P':
            for x in range(1, quantity +1):
                self.__rented_cars.append(self.__petrol_cars.pop())
        elif type == 'E':
            for x in range(1, quantity +1):
                self.__rented_cars.append(self.__electric_cars.pop())
        elif type == 'D':
            for x in range(1, quantity +1):
                self.__rented_cars.append(self.__diesel_cars.pop())
        elif type == 'H':
            for x in range(1, quantity +1):
                self.__rented_cars.append(self.__hybrid_cars.pop())
        self.save_csv(self.get_all_cars_list())
        

    def returnCar(self, type, quantity):
        if type == 'P':
            for x in range(1, quantity +1):
                self.__petrol_cars.append(self.__rented_cars.pop())
        elif type == 'E':
            for x in range(1, quantity +1):
                self.__electric_cars.append(self.__rented_cars.pop())
        elif type == 'D':
            for x in range(1, quantity +1):
                self.__diesel_cars.append(self.__rented_cars.pop())
        elif type == 'H':
            for x in range(1, quantity +1):
                self.__hybrid_cars.append(self.__rented_cars.pop())
        self.save_csv(self.get_all_cars_list())

    def mainMenu(self):
        print('Welcome to Dublin Business School')       
        msg = 'Would you like to rent a car R, return a car U, any key to quit? '
        answer = input(msg)
        while answer.upper() == 'R' or answer.upper() == 'U':
            if answer.upper() == 'R':
                type = input('What car would you like to rent. Please enter P for petrol, E for electric, D for Diesel and H for Hybrid? ')
                quantity = int(input("How many cars you would like to rent? "))
                isInStock = self.checkDesireCarInStock(type.upper(), quantity)
                if isInStock:                    
                    self.rent(type.upper(), quantity)
            elif answer.upper() == 'U':
                type = input('What car would you like to return. Please enter P for petrol, E for electric, D for Diesel and H for Hybrid? ')
                quantity = int(input("How many cars you would like to rent? "))
                self.returnCar(type.upper(), quantity)
            self.checkCarsInStock()
            answer = input(msg)
