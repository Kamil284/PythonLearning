def trasa():
    try:
        ilosc_pasazerow = int(input("Podaj liczbę pasażerów: "))
        dystans = float(input("Podj dystans w kilometrach: "))
        spalanie = float(input("Podaj średnie spalanie samochodu w litrach: "))
        cena_paliwa = float(input("Podaj cene za litr paliwa w PLN: "))

        koszt_paliwa = (dystans / 100) * spalanie * cena_paliwa
        koszt_na_osobe = koszt_paliwa / ilosc_pasazerow

        print(f"Koszt przejazdu wynosi: {round(koszt_paliwa, 2)} zł.")
        print(f"Koszt przejazdu na osobe wynosi: {round(koszt_na_osobe, 2)} zł.")

    except ValueError:
        print("Wprowadzone dane są błędne!")


trasa()
