import random
import time


def orzelReszka(szansaNaTrafienie): #definiowanie funkcji do losowania dwoch zmiennch
    rzut = random.uniform(0, 100)
    if (rzut < szansaNaTrafienie):
        return "Orzeł"
    else:
        return "Reszka"

print("Chcesz rozpocząć? Tak/Nie")

while True:

    start = input()
    start = start.capitalize()
    if start == "Tak":
        orzelReszka(50) #50% szans na wylosowanie ktorejs z odpowiedzi
    else:
        break

    print("Trwa losowanie...")



    print("Chesz rzucić ponownie? Tak/Nie")
