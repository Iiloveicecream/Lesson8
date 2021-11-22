"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой."""


class MyDivisionByZero:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        try:
            return self.a / self.b
        except:
            print('Деление на ноль')

 
division = MyDivisionByZero(1, 0)
print(division.div())
