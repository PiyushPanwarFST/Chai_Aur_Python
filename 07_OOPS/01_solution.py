# 1: creating a class & object
class Car:
    count_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.count_car += 1

    def get_brand(self):
        return self.__brand + "!"
    
    # 2: method that gives full_nae of a Car
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol & disel"
    
    # 3: add a static method to a class that add genral description
    @staticmethod
    def genral_description():
        return "car are means of transport"
    
    # 8: Use a property decorator to make the model attribute read-only.
    @property
    def model(self):
        return self.__model

# self is a kind of telephone line which connect constructor(__init__) method & obj.

# my_nexon = Car("Tata", "Nexon")
# print(my_car.brand)
# print(my_car.model)
# my_car.full_name()


# 3: creating a inherit class
class Electric_Car(Car):
    def __init__(self, brand, model, battry_size):
        super().__init__(brand, model)
        self.battry_size = battry_size

    def fuel_type(self):
        return "electric charge"
    

# my_tesla = Electric_Car("Tesla", "Modle S", "85kwh")
# print(my_tesla.full_name())


# 4: encapsulation private variables & getter methods
# print(my_tesla.__brand)
# print(my_tesla.get_brand())


# 5: polymorphism 
# print(my_nexon.fuel_type())
# print(my_tesla.fuel_type())


# 6: add class variable to class for tracting no. of car created
# print(Car.count_car)
# my_nexon = Car("Tata", "Nexon")
# my_that = Car("Mahindra", "Thar")
# print(Car.count_car)

# 7
# print(Car.genral_description())

# 8 in property decorator we use to access methods just like property
# my_car = Car("Tata", "Nexon")
# my_car.model = "curv"
# print(my_car.model)


# 9 check if my_tesla is an instance of Car and ElectricCar.
my_tesla = Electric_Car("Tesla", "Modle S", "85kwh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, Electric_Car))


# 10 
class Battry:
    def battry_info(self):
        return "battry information"

class Engine:
    def engine_info(self):
        return "engine information"

class Electric_Car_Two(Battry, Engine, Car):
    pass

my_tesla_2 = Electric_Car_Two("tesla", "model s")
print(my_tesla_2.battry_info())
print(my_tesla_2.engine_info())
