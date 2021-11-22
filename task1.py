"""1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода
Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Date:

    def __init__(self, date):
        self.day, self.mouth, self.year = date.split('-')

    @classmethod
    def date_to_int(cls, date_as_string):
        data_int = cls(date_as_string)
        return int(data_int.day), int(data_int.mouth), int(data_int.year)

    @staticmethod
    def valid_date(date_as_string):
        day, mouth, year = map(int, date_as_string.split('-'))
        return 0 < day <= 31, \
               0 < mouth <= 12, \
               year < 2022


print(Date.valid_date('31-5-2002'))
print(Date.date_to_int('31-5-2002'))
