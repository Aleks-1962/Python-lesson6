""" Реализуем базовый класс Stationary. Описываем дочерние классы Pen, Pencil, Handle.
Переопределяем для все дочерних классов метод draw"""


class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск метода отрисовки {self.title}'


class Pen(Stationary):

    def draw(self):
        return f'Метод отрисовки - {self.title}'


class Pencil(Stationary):

    def draw(self):
        return f'Метод отрисовки - {self.title}'


class Handle(Stationary):

    def draw(self):
        return f'Метод отрисовки - {self.title}'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
