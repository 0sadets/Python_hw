import time

users_dict = {
    "user1":"qwerty1",
    "user2":"ytrewq!",
    }

def add_new_user(login, psw):
    if login in users_dict:
        print(f"{login} is already exist")
    else:
        users_dict[login] = psw
        print(f"{login} added")

def delete_user(key):
    if key in users_dict:
        users_dict.pop(key)
        print(f"{key} deleted")
    else: 
        print(f"There is no {key} user")
        
def change_psw(key, new_psw):
    if key not in users_dict:
        print(f"There is no {key} user")
        return
    if users_dict[key] == new_psw:
        print(f"old key = new key")
    else:
        users_dict[key] = new_psw
        print("password changed")

def check_psw():
    for key, val in users_dict.items():
        if len(val) < 6 or val.isalpha():
            print(f"{key} має незахищений пароль: {val}")

def show_users():
    print("user list:")
    for login, psw in users_dict.items():
        print(f"{login}: {psw}")

def main():
    while True:
        print("Enter option:")
        print("1. add new user")
        print("2. delete user")
        print("3. change password")
        print("4. check passwords")
        print("5. get user list")
        print("6. exit")
        choice = input("Enter(1-6): ")
        if choice == '1':
            login = input("enter login: ")
            psw = input("enter psw: ")
            add_new_user(login, psw)
        elif choice == '2':
            login = input("enter login: ")
            delete_user(login)
        elif choice == '3':
            login = input("enter login: ")
            psw = input("enter new psw: ")
            change_psw(login, psw)
        elif choice == '4':
            check_psw()
        elif choice  == '5':
            show_users()
        elif choice =='6':
            print("bye")
            break
        else: 
            print("invalid choice")
        return main()
        
#main()


# ___________________________________________________________________
def time_decor(func):
    def output_func():
        start = time.time()
        res = func()
        print(f"time: {time.time() - start:.8f} ")
        return res
    return output_func
@time_decor
def get_even():
    even_numbers = []  
    for i in range(100000):  
        if i % 2 == 0: 
            even_numbers.append(i)  
    return even_numbers
numbers = get_even()
print("even nums:")
# print(numbers)