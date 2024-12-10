# Завдання 1:
# Створіть декоратор, який виправляє вхідні параметри функції. Декоратор визначає
# всі числові параметри які приходять у функцію та всі, що менше 0, замінює на 1.
# Наприклад: func(10, -3, “red”, -1, 200) -> func(10, 3, “red”, 1, 200)

def change_neg(func):
    def wrapper(*args):
        new_args = []
        for a in args:
            if type(a) != str:
                new_args.append(1) if a < 0 else new_args.append(a)
                # if a < 0:
                #     new_args.append(1)
                # else:
                #     new_args.append(a)
            else: new_args.append(a)
        return func(*new_args)
    return wrapper

@change_neg
def showInfo(*args):
    print(args)

showInfo(10, -3, 'red', -1, 200)