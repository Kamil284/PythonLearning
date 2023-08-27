print("Wybierz znak")
wybor = input("* mnozenie / dzielenie + dodawanie - odejmowanie ^ - potegowanie ")

a = int(input("Pierwsza liczba "))
b = int(input("Druga liczba "))

if wybor == '*':
    print(a * b)
elif wybor == '/':
    if b == 0:
        print("Nie dzielimy przez 0")
    else:
        print(int(a / b))
elif wybor == '+':
    print(a + b)
elif wybor == '-':
    print(a - b)
elif wybor == '^':
    print(a ** b)
else:
    print("Nie wybrałeś zadnej z możliwych opcji, spróbuj ponownie")

x = int(input("wprowadz liczbe "))
if x < 0:
    x = -x
    print(x)
elif x >= 0:
    print(x)
if (5 > 7):
    print("first ")
    print("second")