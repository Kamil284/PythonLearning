class User:
    def __init__(self, name: str, surname: str, date_birth: int):
        self.name = name
        self.surname = surname
        self.date_birth = date_birth

users = []

def user_add():
    print('Add new user ')
    name = input('Name: ')
    surname = input('Surname: ')
    date_birth = input('Date of birth: ')
    new_user = User(name, surname, date_birth)
    users.append(new_user)
    print('User add completled.')

def view_users():
    print("Users: ")
    for i, user in enumerate(users, start=1):
        print(f"{i}. Name: {user.name}, Surname: {user.surname}, Year of birth: {user.date_birth}")

while True:
    print("Choice number: ")
    print("1. User add")
    print("2. View users")
    print("3. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        user_add()
    elif choice == "2":
        view_users()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Your choice is wrong")