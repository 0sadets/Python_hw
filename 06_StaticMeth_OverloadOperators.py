'''
Створіть клас для конвертування температури з Цельсія у Фаренгейт, і навпаки. 
У класі має знаходитися два статичні методи: для конвертування з Цельсія у Фаренгейт 
і для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати кількість 
підрахунків температури та повернути це значення статичним методом.
'''
class ConvertTemperature():
    _convertCount = 0
    @staticmethod
    def c_to_f(cel):
        if isinstance(cel, (int, float)):
            faren = (cel*1.8)+32
        else: 
            print(f"'{cel}' is invalid number") 
            return None
        ConvertTemperature._convertCount += 1
        return faren
        

    @staticmethod
    def f_to_c(far):
        if isinstance(far, (int, float)):
            cels = (far - 32)/1.8
        else: 
            print(f'"{far}" is nor valid number')
            return None
        ConvertTemperature._convertCount += 1
        return cels
    @staticmethod
    def convert_count():
        return ConvertTemperature._convertCount


def main():
    while True:
        answ = int(input(f"Choose option:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Exit\n"))
        if answ == 1:
            temp_c = int(input("Enter Celsius: "))
            temp_f = ConvertTemperature.c_to_f(temp_c)
            print(f"{temp_c} C = {temp_f} F")
        elif answ == 2:
            temp_f = int(input("Enter Fahrenheit: "))
            temp_c = ConvertTemperature.f_to_c(temp_f)
            print(f"{temp_f} F = {temp_c} C")
        elif answ == 3:
            break
        else:
            print(f"{answ} is invalid Choice. Try again.")
            main()

#main()
'''
Створіть клас Airplane (Літак). За допомогою перевантаження операторів, реалізуйте:
• перевірку на рівність типів літаків (операція ==);
• збільшення та зменшення пасажирів у салоні літака (операції +, -, +=, -=);
• порівняння двох літаків за максимально можливою кількістю пасажирів на борту (операції >, <, <=, >=).
'''

class Airplane():
    def __init__(self, type, pass_count, max_pass_count):
        self.type = type
        self.passanger_count = pass_count
        self.max_count = max_pass_count
    def __eq__(self, other):
        return self.type == other.type
    def __add__(self, num):
        if isinstance(num, int):
            new_count = self.passanger_count + num 
            if new_count > self.max_count:
                print(f"Cant add {num} passengers - exceeds the maximum number of passengers")
                return self
            return Airplane(self.type, new_count, self.max_count)
        else: print("You can only add an integer number of passengers")
    def __sub__(self, num):
        if isinstance(num, int):
            new_count = self.passanger_count - num
            if new_count<0:
                print(f"Count of passengers < 0")
                return self
            return Airplane(self.type, new_count, self.max_count)
        else: print("You can only sub an integer number of passengers")
    def __iadd__(self, num):
        if isinstance(num, int):
            new_count = self.passanger_count + num 
            if new_count > self.max_count:
                print(f"Cant add {num} passengers - exceeds the maximum number of passengers")
                return self
            return Airplane(self.type, new_count, self.max_count)
        else: print("You can only add an integer number of passengers")
    def __isub__(self, num):
        if isinstance(num, int):
            new_count = self.passanger_count - num
            if new_count<0:
                print(f"Count of passengers < 0")
                return self
            return Airplane(self.type, new_count, self.max_count)
        else: print("You can only sub an integer number of passengers")
    def __it__(self, other):
        return self.max_count < other.max_count
    def __le__(self, other):
        return self.max_count <= other.max_count
    def __gt__(self, other):
        return self.max_count > other.max_count
    def __ge__(self, other):
        return self.max_count >= other.max_count
    def __str__(self):
        return f"type: {self.type}\npassenger count: {self.passanger_count}\nmaxpassenger count: {self.max_count}"

ar1 = Airplane("a123", 50, 50) 
ar2 = Airplane("a123", 43, 60) 
ar3 = Airplane("boing", 21, 55) 
ar4 = Airplane("mriya", 24, 70) 
print(ar1)
ar1 += 5
print(ar1)
ar1 -= 5
print(ar1)

print(ar1==ar2)
print(ar1==ar3)
print(ar1>ar4)
print(ar3<ar2)
