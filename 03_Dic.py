'''
Завдання 1
Створіть програму, що містить інформацію про відомих
баскетболістів. Збережіть ПІБ та зріст кожного баскетболіс-
та. Реалізуйте можливість додавати, видаляти, знаходити та
змінювати дані. Використовуйте словник для збереження
інформації.
Завдання 2
У словнику зберігається набір пар: Назва країни ->
Столиця. Реалізуйте функціональність за додаванням,
видаленням, пошуком, заміною.
'''
dic_players = {"boy1":191, "boy2":186, "boy3": 198, "boy4": 197}
dic_countries = {"Ukraine":"Kyiv", "Spain":"Madrid", "Italy":"Rome", "Japan":"Tokio"}

def add_p(name, h): dic_players[name] = h
def add_c(name, c): dic_countries[name] = c

def remove_p(name): dic_players.pop(name)
def remove_c(name): dic_countries.pop(name)

def find_p(name): return dic_players.get(name, "no player founf")
def find_c(name): return dic_countries.get(name, "no country founf")

def update_p(name, h):
    if name in dic_players:
        dic_players[name] = h
    else:
        print("no player found")
def update_c(name, c):
    if name in dic_countries:
        dic_countries[name] = c
    else:
        print("no player found")


def first_task():
    while(True):
        print(f"We have {dic_players}")
        print("1. add\n2. remove\n3. find\n4. update\n5. exit")
        choice = int(input("Choice: "))
        if choice == 5: return
        else:
            if choice == 1:
                n = input("Enter new name: ")
                h = int(input("Enter new height: "))
                add_p(n,h)
            elif choice == 2:
                n = input("Enter name to remove: ")
                remove_p(n)
            elif choice ==4:
                n = input("Enter new name: ")
                h = int(input("Enter new height: "))
                update_p(n,h)
            elif choice ==3:
                n = input("Enter name to search: ")
                print(f"We found {n}: {find_p(n)}")
            else:
                print("Invalid choice. Try again.")
                first_task()
def second_task():
    while(True):
        print(f"We have {dic_countries}")
        print("1. add\n2. remove\n3. find\n4. update\n5. exit")
        choice = int(input("Choice: "))
        if choice == 5: return
        else:
            if choice == 1:
                n = input("Enter new Country: ")
                c = input("Enter new Capital: ")
                add_c(n,c)
            elif choice == 2:
                n = input("Enter Country to remove: ")
                remove_c(n)
            elif choice ==4:
                n = input("Enter new Country: ")
                c = input("Enter new Capital: ")
                update_c(n,c)
            elif choice ==3:
                n = input("Enter Country name to search: ")
                print(f"We found {n}: {find_c(n)}")
            else:
                print("Invalid choice. Try again.")
                second_task()

def main():
    first_task()
    second_task()

main()