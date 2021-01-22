""" Реализуем класс Road (дорога), c защищенными атрибутами: length (длина), width (ширина).
Значения данных атрибутов передаются при создании экземпляра класса.
Определяем метод расчета массы асфальта, для покрытия дорожного полотна."""


class Road:

    def __init__(self, _length, _width, weight, height):
        self._length = _length    # защищенный
        self._width = _width   # защищенный
        self.weight = weight
        self.height = height

    def massa(self):
        mass = self._length * self._width*self.weight * self.height/1000
        return f'Для покрытия дорожного полотна {self._length/1000} км,' \
               f' шириной {self._width} м и ' \
               f'толщиной {self.height} см, ' \
               f'необходимо {round(mass)} тн асфальта'


r = Road(10000, 15, 25, 10)
print(r.massa())
