from abc import ABCMeta, abstractmethod
class IgnitionKey:

    def start_drive(self):
        pass


class IgnitionButton:

    def start_drive(self):
        pass


class Car(metaclass=ABCMeta):

    @abstractmethod
    def create_starter(self):
        raise NotImplementedError

    def drive(self):
        starter = self.create_starter()
        starter.start_drive()


class Volvo(Car):

    name = 'Volvo'

    def __str__(self):
        return 'Volvo'

    def create_starter(self):
        return IgnitionButton()


class Lada(Car):

    name = 'Lada'

    def __str__(self):
        return 'Lada'

    def create_starter(self):
        return IgnitionKey()


