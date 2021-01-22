""" Реализуем базовый класс Car. Описываем дочерние классы TownCar, SportCar, WorkCar, PoliceCar.
Для классов TownCar и WorkCar переопределите метод """


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        self.direction = direction
        return f'Машина {self.name} повернула'

    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.show_speed}'


class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return f'Машина - {self.speed} превысила скорость в городе!!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):

        if self.speed > 40:
            return f'Машина - {self.speed} превысила разрешенную скорость в городе!!'


class PoliceCar(Car):
    pass


tw = TownCar('Шкода', 70, 'белая', True)
print('Городская' + tw.go(), tw.show_speed(), tw.turn(' налево'), tw.stop())

sp = SportCar('Порше', 170, 'красная', False)
print('Спортивная' + sp.go(), sp.show_speed(), sp.stop())

wr = WorkCar('МАЗ', 30, 'хаки', True)
print('Рабочая' + wr.go(), wr.show_speed(), wr.turn(' право'), wr.stop())

pl = PoliceCar('Форд', 100, 'бело-синия', True)
print('Полиция' + pl.go(), pl.show_speed(), pl.turn('направо'), pl.turn(' налево'), pl.stop())
