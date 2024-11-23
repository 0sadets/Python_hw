'''
Завдання 1
Користувач вводить з клавіатури назву фрукта. Ви-
ведіть на екран кількість фруктів, що містяться в кортежі як елемент.
Завдання 2
Додайте до першого завдання підрахунок кількості,
коли назва фрукта є частиною елемента. Наприклад,
banana, apple, bananamango, mango, strawberry-banana.
У приведеному прикладі banana попадається три рази.
Завдання 3
Маємо кортеж з назвами автовиробників (назва ви-
робника може зустрічатися від 0 до N разів). Користувач
вводить з клавіатури назву виробника та слово для заміни.
Замініть в кортежі усі елементи з цією назвою на слово
для заміни. Збіг за назвою має бути повним.
Завдання 4
Маємо кортеж з цілими числами. Виведіть статистику
за кількістю цифр в елементах кортежу. 
Наприклад:
Одна цифра — 3 елементи
Дві цифри — 4 елементи
Три цифри — 5 елементів
'''

def task_1(fruits):
    name = input("Enter fruit name: ")
    count = fruits.count(name)
    print(f"The fruit '{name}' appears {count} times in the tuple.")

def task_2(fruits):
    name = input("Enter fruit name: ")
    count =0 
    for f in fruits:
        if name in f:
            count = count + 1
    print(f"The fruit '{name}' appears {count} times in the tuple.")

def task_3():
    cars = ("Mazda", "BMW", "Audi", "Mitsubishi", "Volvo", "Toyota", "Audi")
    car_name = input("Enter car name: ").lower()
    new_name = input("Enter new car name: ")
    new_tuple = []
    for car in cars:
        if car.lower() == car_name:
            new_tuple.append(new_name)
        else:
            new_tuple.append(car)
    new_tuple = tuple(new_tuple)
    print("Original tuple:", cars)
    print("Updated tuple:", new_tuple)


def task_4():
    nums = (1, 5, 45, 78, 456, 465, 132, 1325, 4568)
    one_digit = 0
    two_digits = 0
    three_digits = 0
    four_digits = 0
    for n in nums:
        num_digits  = len(str(n))
        if num_digits == 1:
            one_digit += 1
        elif num_digits == 2:
            two_digits += 1
        elif num_digits == 3:
            three_digits += 1
        elif num_digits == 4:
            four_digits += 1
    if one_digit > 0:
        print(f"one digit: {one_digit} elements")
    if two_digits > 0:
        print(f"two digits: {two_digits} elements")
    if three_digits > 0:
        print(f"three digits: {three_digits} elements")
    if four_digits > 0:
        print(f"four digits: {four_digits} elements")





def main():
    fruits = ("apple", "pear", "kivi", "apple", "banana", "banana", "pear", "apple", "bananamango", "strawberry-banana")
    task_1(fruits)
    task_2(fruits)

    task_3()

    task_4()

main()