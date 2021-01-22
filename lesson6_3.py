""" Реализуем базовый класс Worker. Создаем дочерний класс Position на базе Worker
В классе Position реализуем методы полное имя и доход сотрудника."""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Сотрудник - {self.surname} {self.name}'

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


pers = Position('Василий', 'Смирнов', 'разнорабочий IT', 150000, 50000)
print(pers.get_full_name(), pers.position, 'зарабатывает', pers.get_total_income())
pers = Position('Василий', 'Смирнов', 'разнорабочий автопрома', 15000, 5000)
print('А ', pers.get_full_name(), pers.position, 'зарабатывает', pers.get_total_income())
