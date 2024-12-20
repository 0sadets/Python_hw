'''
ГЕНЕРАТОРИ
Створіть функцію, яка повертає всі непарні числа в діапазоні.
Функція приймає початок і кінець діапазону як параметри.
Використовуйте механізм генераторів усередині функції.
'''

def odd_func(start, end):
    # Використовуючи оператор yielf
    for i in range(start, end):
       if( i % 2 != 0): yield i
    # Використовуючи спискові включення:
    return [i for i in range(start, end) if i%2!=0]

# start = int(input("Enter start: "))
# end = int(input("Enter end: "))

# for i in odd_func(start, end):
#     print(i)

'''
Завдання 1:
Створіть клас Passport (паспорт), який міститиме паспортну інформацію про
громадянина України. (мінімум 5 властивостей).
За допомогою механізму успадкування реалізуйте клас ForeignPassport
(закордонний паспорт), похідний від Passport.
Закордонний паспорт містить, крім паспортних даних, дані про візи і
номер закордонного паспорта.
Кожен із класів має містити необхідні методи. Закордонний повинен містити колекцію віз,
методи додавання та видалення візи. 
Також забезпечити класи методами
перетворення до str.
'''
class Passport():
    def __init__(self, name, surname, country, age, number):
        self.name = name
        self.surname = surname
        self.country = country
        self.age = age
        self.number = number
    def __str__(self):
        return f"{self.name} {self.surname} {self.age}y.o. \n{self.country} \nnumber: {self.number}"


class ForeignPassport(Passport):
    def __init__(self, name, surname, country, age, number, foreign_number):
        super().__init__(name, surname, country, age, number)
        self.visas = []
        self.foreign_number = foreign_number
    def __str__(self):
        return super().__str__() + f' \nVisas: {self.visas}  \nNumber: {self.foreign_number}'
    def add_visa(self, visa):
        self.visas.append(visa) 
    def del_visa(self, visa):
        if(visa in self.visas):
            self.visas.remove(visa)
        else: print(f"No {visa} found")
        
psp = Passport("Olexandra", 'Osadets', "Ukraine", 20, "123456789" ) 
print(psp)
f_psp = ForeignPassport("Max", "Sokol", "Ukraine", 20, '123456789', '987654321')
f_psp.add_visa("im visa to some country")
f_psp.add_visa("im visa to another country")
f_psp.add_visa("im visa to one more country")
print(f_psp)