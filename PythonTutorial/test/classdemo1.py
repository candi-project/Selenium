class Car(object):
    wheel = 4

    def __init__(self, name, model):
        self.name = name
        self.model = model
        print('You are awesome.')

    def info(self):
        print("Maker of the car: " + self.name)
        print("Model of the car: " + self.model)

    def drive(self):
        print('Car drive..')


class Audi(Car):
    def __init__(self, name, model):
        Car.__init__(self, name, model)
        print("Class Audi.")

    def info(self):
        super(Audi, self).info()
        print('info yea')


# print(Car.wheel)
# c1 = Car('BMW', '1234')
# print(c1.name)
# print(c1.model)
# c1.info()

b = Audi('a', 'b')
b.info()
# b.drive()