from factory_method.factory_method import Volvo, Lada


class CarNotFoundException(Exception):
    pass


class CarFactory:

    CARS = [Volvo, Lada]

    def create_car(self, car_name):
        for car in self.CARS:
            if car_name.lower() == car.name.lower():
                return car()
        raise CarNotFoundException('Car not found: {car_name}'.format(car_name=car_name))


class TestDrive:

    def __init__(self, car_factory):
        self.factory = car_factory

    def go(self, car_name):
        print('driving {car_name}'.format(car_name=car_name))
        self.factory.create_car(car_name)


if __name__ == '__main__':

    test_drive = TestDrive(CarFactory())

    test_drive.go('volvo')
