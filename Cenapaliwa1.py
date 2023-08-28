def koszt_drogi(km,sp,cp): #km=ilosc kilometrow sp=spalanie na 100km cp=cena paliwa
    return km / sp * cp
def ilosc_osob(km,sp,cp,os): ##km=ilosc kilometrow sp=spalanie na 100km cp=cena paliwa os=ilosc osob
    return (km / sp * cp) / os

while(True):
    print("Wybierz: ")
    print('"1" jeżeli jedziesz sam')
    print('"2" jeżeli jedziesz z kimś')
    wybor = input("Wprowadz liczbe: ")
    if wybor == "1":
        km = float(input("Wprowadz ilość kilometrów do przejechania: "))
        sp = float(input("Wprowadz spalanie na 100km: "))
        cp = float(input("Wprowadz cene paliwa za jeden litr w PLN: "))
        print("Kosz przejchania tej trasy wynosi", round(koszt_drogi(km, sp, cp), 2))
        break
    elif wybor == "2":
        km = float(input("Wprowadz ilość kilometrów do przejechania: "))
        sp = float(input("Wprowadz spalanie na 100km: "))
        cp = float(input("Wprowadz cene paliwa za jeden litr w PLN: "))
        os = float(input("Wprowadz liczbe osób w samochodzie: "))
        print("Kosz przejchania tej trasy dla", int(os), "osób wynosi", round(ilosc_osob(km, sp, cp, os),2), "na osobe")
        break
    else:
        print("Nie wybrałeś poprawnej opcji.\n" "Spróbuj ponownie!\n")
        continue
