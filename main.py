class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.fuel = 0

    def refuel(self,liters):
        if liters <= 0:
            print("Нельзя добавить ноль или отрицательное коичество топлива")
            return
        self.__fuel +=liters

    def drive(self,km):
        needed = km * 0.1
        if needed > self.__fuel:
            print("Не хватает топлива")
            return
        self.__fuel -=needed
        print(f"Проехали{km}км")

    def info(self):
        return f"{self.brand} {self.model} топлива: {self.__fuel:g},л"

    car1 = car=("Daewo", "Nexia 3")
    car2 = car("Chevrolet", "Cobalt")

    car1.refuel(12)
    print(car1.info())

    car1.refue(-5)
    car1.drive(50)
    print(car1.info())

    car2.drive(10)
    car2.refuel(20)
    car2.druve(100)
    print(car2.info)
    
    
        