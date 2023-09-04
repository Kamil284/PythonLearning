import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#pusty slownik na login i haslo
users = {}

#definiowanie rejestracji nowych uzyt
def register():
    user_name = input("Wpisz nazwe uzytkownika: ")
    password = input("Wprowadz haslo: ")
    hashed_password = hash_password(password)
    users[user_name] = hashed_password
    print("Udalo ci sie zarejestrowac.")

#definiowanie logowania
def login():
    user_name = input("Podaj nazwe uzytkownika: ")
    password = input("Wprowadz haslo: ")
    hashed_password = hash_password(password)
    if users.get(user_name) == hashed_password:
        print("Udalo ci sie zalogowac do konta! :)")
    else:
        print("Bledna nazwa uzytkownika albo haslo")

while True:
    print("1 Rejestracja")
    print("2 Logowanie")
    print("3 Koniec")

    wybor = input("Wybierz")
    if wybor == "1":
        register()
    elif wybor == "2":
        login()
    elif wybor == "3":
        break
    else:
        print("Nie wybrales poprawnie")



