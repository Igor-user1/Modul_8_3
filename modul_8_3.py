class Car:

    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) and vin_number in range(1000000, 10000000):
            return True
        elif not isinstance(vin_number, int):
            raise IncorrectVinNumber(f"Неккоректный тип vin номер")
        else:
            raise IncorrectVinNumber(f"Неверный диапазон для vin номера")

    def __is_valid_numbers(self, __numbers):
        if isinstance(__numbers, str) and len(__numbers) == 6:
            return True
        elif not isinstance(__numbers, str):
            raise IncorrectCarNumbers(f"Некорректный тип данных для номеров")
        else:
            raise IncorrectCarNumbers(f"Неверная длина номера")


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

  try:
      second = Car('Model2', 300, 'т001тр')
  except IncorrectVinNumber as exc:
      print(exc.message)
  except IncorrectCarNumbers as exc:
      print(exc.message)
  else:
      print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
