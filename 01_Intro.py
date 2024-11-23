'''
Завдання 1
Користувач вводить із клавіатури число. Необхідно перевірити його
на парність і непарність. Якщо число парне, потрібно вивести на 
екран число і напис Even number. Якщо число непарне виведіть на 
екран число і напис Odd number.

Завдання 2
Користувач вводить із клавіатури число. Необхідно перевірити 
його на кратність 7. Якщо число кратне, потрібно вивести на 
екран число і напис Number is a multiple of 7. Якщо число не 
кратне, виведіть на екран число і напис Number is not a multiple of 7.

Завдання 3
Користувач вводить із клавіатури два числа. Необхідно знайти 
максимум із двох чисел і вивести його на екран.

Завдання 4
Користувач вводить із клавіатури два числа. Необхідно знайти 
мінімум із двох чисел і вивести його на екран.

Завдання 5
Користувач вводить із клавіатури два числа. Залежно від вибору 
користувача потрібно показати суму двох чисел, різницю двох чисел, 
середньоарифметичне або добуток двох чисел.
'''



def task_1(num):
    return "is even." if num%2==0 else " is odd."
    

def task_2(num):
    return " " if num%7 == 0 else "not"

def task_3(a,b):
    if (a==b): return f"both are the same ({a} = {b})"
    return a if a>b else b

def task_4(a,b):
    if(a==b): return f"both are the same ({a} = {b})"
    return a if a<b else b

def functions(a,b, symb):
    if(symb=="+"): 
        print(f"{a} + {b} = {a+b}") 
    elif(symb=="-"): 
        print(f"{a} - {b} = {a-b}")
    elif(symb=='*'): 
        print(f"{a} * {b} = {a*b}")
    elif(symb == "avg"): 
        print(f"({a} + {b})/2 = {(a+b)/2}")
    else:
        print("Invalid input. Please try again.") 

def task_5(a,b):
    while True:
        symb = input("Enter '+' or '-' or '*' or 'avg'\n '0' - to leave. \n ")
        
        if(symb == "0"): 
            return "Goodbye"
        else:
            functions(a,b,symb)
            return task_5(a,b)





def main():
    print(f'------------Task {1}-------------')
    num = int(input("Enter your number: "))
    print(f"{num} {task_1(num)}")


    print(f'------------Task {2}-------------')
    num = int(input("Enter your number: "))
    print(f"Number {num} is {task_2(num)} a multiple of 7.")


    print(f'------------Task {3}-------------')
    num1 = int(input("Enter a: "))
    num2 = int(input("Enter b: "))
    print(f"The max num is: {task_3(num1,num2)}")


    print(f'------------Task {4}-------------')
    num1 = int(input("Enter a: "))
    num2 = int(input("Enter b: "))
    print(f"The min num is: {task_4(num1,num2)}")


    print(f'------------Task {5}-------------')
    num1 = int(input("Enter a: "))
    num2 = int(input("Enter b: "))
    print(task_5(num1, num2))


main()