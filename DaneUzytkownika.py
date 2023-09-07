class User:
    def __init__(self, name, surname, date_birth):
        self.name = name
        self.surname = surname
        self.date_birth = date_birth

users = []

def user_add():
    print('Add new user ')
    name = input('Name: ')
    surname = input('Surname: ')
    date_birth = input('Date of birth: ')
    new_user = users(name, surname, date_birth)
    users.append(new_user)
    print('User add completled.')

def 