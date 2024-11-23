'''
Завдання 1

Маємо множину з назвами країн. Надайте користу-
вачеві можливість:
■ додавати країни;
■ видаляти країни;
■ пошуку країн за введеними символами;
■ перевіряти, чи міститься країна в множині.
Завдання 2
Маємо дві множини з назвами міст. Створіть третю
множину з тими назвами, які є в обох множинах.
Завдання 3
Маємо дві множини з назвами міст. Створіть третю
множину з тими назвами, які містяться в першій множині,
але відсутні у другій.
Завдання 4
Маємо дві множини з назвами міст. Створіть третю
множину з тими назвами, які містяться в другій множині,
але відсутні в першій.
Завдання 5
Маємо дві множини з назвами міст. Створіть третю
множину з унікальними назвами для кожної множини.
'''
countries = {"Ukraine", "Spain", "Paris", "USA", "Thailand", "Japan", "Korea", "Netherlands", "Denmark"}
city1 = {"Kyiv", "Rivne", "Kharkiv"}
city2 = {"Rivne", "Lviv", "Kyiv"}

def print_c(): print(countries)

def add_c(c): countries.add(c)
 
def delete_c(c): countries.discard(c)

def search_by_symb(symb):
    for c in countries:
        if symb.lower() in c.lower():
            return print(f"We found country: {c}")

def is_in_set(c): return c in countries
  
def first_task():
    while(True):
        print("1. add new country")
        print("2. delete  country")
        print("3. search country by symb")
        print("4. search country by country name\n5. exit")
        us_choice = int(input("Your choice: "))
        if(us_choice == 5): return False
        else:
            if(us_choice==1):
                c = input("Enter New Country: ")
                add_c(c)
            elif(us_choice==2):
                c = input("Enter Country name to delete: ")
                delete_c(c)
            elif(us_choice==3):
                c = input("Enter symbols to search country: ")
                search_by_symb(c)
            elif(us_choice==4):
                c = input("Enter country to search in set: ")
                print(f"Country {c} in set: {is_in_set(c)}")
            else:
                print("Invalid Choice. Try again.")
            print_c()
            return first_task()

def second_task(): return city1&city2

def third_task(): return city1-city2

def fourth_task(): return city2-city1

def main():
    first_task()
    print(f"city1 & city2 =  {second_task()}")
    print(f"city1 - city2 =  {third_task()}")
    print(f"city2 - city1 =  {fourth_task()}")
    print(f"Unique names for each set: {third_task()}, {fourth_task()}")

    

main()

