"""Создаем класс TrafficLight (светофор) и определяем у него один атрибут color (цвет) и метод running (запуск).
 Атрибут реализуем как приватный.
 В рамках метода реализуем переключение светофора в режимы: красный, желтый, зеленый. """

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        print('Светофор включился')
        while i < 3:
            print('Цвет светофора - ', end=' ')
            if i == 0:
                print(TrafficLight.__color[i])
                sleep(7)
                print('Светофор переключается')
            elif i == 1:
                print(TrafficLight.__color[i])
                sleep(2)
                print('Светофор переключается')
            elif i == 2:
                print(TrafficLight.__color[i])
                sleep(9)
            i += 1
        print('Светофор выключился')

t_light = TrafficLight()
t_light.running()
