# Завдання 1:
# Створіть додаток для управління користувачами, який має зберігати наступну
# інформацію:
# • логіни користувачів;
# • паролі користувачів.
# Для зберігання інформації використовуйте словник.
# Додаток має надавати таку функціональність:
# • додати нового користувача;
# • видалити користувача;
# • змінити пароль (приймається лише пароль, який відрізняється від
# попереднього);
# • перевірити паролі (відображається незахищені паролі);
# • отримати інформацію про пароль за логіном користувача;
# • *зберегти список користувачів у файл.
# ! незахищеним паролем вважається такий, що має менше 6-ти символів або лише
# букви
import json
users_dict = {
    "user1":"qwerty1",
    "user2":"ytrewq!",
    }

# • додати нового користувача;
def add_new_user(login, psw):
    if login in users_dict:
        print(f"{login} is already exist")
    else:
        users_dict[login] = psw
        print(f"{login} added")

# • видалити користувача;
def delete_user(key):
    if key in users_dict:
        users_dict.pop(key)
        print(f"{key} deleted")
    else: 
        print(f"There is no {key} user")
        
# • змінити пароль (приймається лише пароль, який відрізняється від попереднього);
def change_psw(key, new_psw):
    if key not in users_dict:
        print(f"There is no {key} user")
        return
    if users_dict[key] == new_psw:
        print(f"old key = new key")
    else:
        users_dict[key] = new_psw
        print("password changed")

# • перевірити паролі (відображається незахищені паролі);
def check_psw():
    for key, val in users_dict.items():
        if len(val) < 6 or val.isalpha():
            print(f"{key} має незахищений пароль: {val}")

# • отримати інформацію про пароль за логіном користувача;
def get_psw_by_login(login):
    if login not in users_dict:
        print(f"There is no {login} user")
        return
    else:
        print(f"{login}`s psw: '{users_dict[login]}'")

def show_users():
    print("user list:")
    for login, psw in users_dict.items():
        print(f"{login}: {psw}")

# • *зберегти список користувачів у файл.
def save(filename):
    with open(filename, "w") as file:
        json.dump(users_dict, file)

def main():
    while True:
        print("Enter option:")
        print("1. add new user")
        print("2. delete user")
        print("3. change password")
        print("4. check passwords")
        print("5. get user list")
        print("6. get user`s psw by login ")
        print("7. save to file ")
        print("8. exit ")
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
        elif choice == '6':
            login = input("enter login: ")
            get_psw_by_login(login)
        elif choice =='7':
            save("file_users")
        elif choice =='8':
            print("bye")
            break
        else: 
            print("invalid choice")
        return main()
        
main()