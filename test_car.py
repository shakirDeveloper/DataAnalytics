import unittest
import random
from ca_2_car_inventory_system import Car, CarFleet, PetrolCar, DieselCar, ElectricCar, HybridCar

# test the car functionality
class TestCar(unittest.TestCase):

    def test_car_mileage(self):
        self.car = Car()
        self.assertEqual(0, self.car.getMileage())
        self.car.setMileage(45)
        self.assertEqual(45, self.car.getMileage())
       
    def test_car_make(self):
        self.car = Car()
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())
    
    def test_car_model(self):
        self.car = Car()
        self.assertEqual('', self.car.getModel())
        self.car.setModel('2019')
        self.assertEqual('2019', self.car.getModel())

    def test_car_colour(self):
        self.car = Car()
        self.assertEqual('', self.car.getColour())
        self.car.setColour('yellow')
        self.assertEqual('yellow', self.car.getColour())

    def test_car_engine_size(self):
        self.petrolCar = PetrolCar()
        self.assertEqual(660, self.petrolCar.getEngineSize())
        self.petrolCar.setEngineSize(2000)
        self.assertEqual(2000, self.petrolCar.getEngineSize())

    def test_electric_car_fuel_cells(self):
        self.electric_car = ElectricCar()
        self.assertEqual(1, self.electric_car.getNumberFuelCells())
        self.electric_car.setNumberFuelCells(4)
        self.assertEqual(4, self.electric_car.getNumberFuelCells())

    def test_hybrid_car_(self):
        self.hybrid_car = HybridCar()
        self.assertEqual(1, self.hybrid_car.getNumberFuelCells())
        self.assertEqual(660, self.hybrid_car.getEngineSize())
        self.hybrid_car.setNumberFuelCells(4)
        self.hybrid_car.setEngineSize(1500)
        self.assertEqual(4, self.hybrid_car.getNumberFuelCells())
        self.assertEqual(1500, self.hybrid_car.getEngineSize())

    def test_car_fleet(self):
        car_list = []
        
        avaliable_colours = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black" ]
        available_makers = [ "toyota", "honda", "suzuki", "bmw", "audi", "kia", "ford", "sokoda" ]
        available_models = [ "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013" ]
        available_mileage = [ "15", "12", "20", "10", "10", "11", "14", "16" ]
        
        colours = [random.choice(avaliable_colours) for i in range(40)]
        makers = [random.choice(available_makers) for i in range(40)]
        models = [random.choice(available_models) for i in range(40)]
        mileages = [random.choice(available_mileage) for i in range(40)]
        
        for i in range(40):
            car = Car()
            car.setColour(colours[i])
            car.setMake(makers[i])
            car.setMileage(mileages[i])
            car.setModel(models[i])
            car_list.append(car)
        
        car_fleet = CarFleet(car_list)
        
        self.assertEqual(20, len(car_fleet.getPetrolCars()))
        self.assertEqual(6, len(car_fleet.getElectricCars()))
        self.assertEqual(10, len(car_fleet.getDieselCars()))
        self.assertEqual(4, len(car_fleet.getHybridCars()))


        car_fleet.rent('P',5)
        self.assertEqual(1, car_fleet.checkDesireCarInStock('P',5))
        self.assertEqual(0, car_fleet.checkDesireCarInStock('P',36))


        car_fleet.returnCar('P',2)
        self.assertEqual(1, car_fleet.checkDesireCarInStock('P',17))


        car_fleet.returnCar('P',3)
        self.assertEqual(40, len(car_fleet.get_all_cars_list()))

if __name__ == '__main__':
    unittest.main()
