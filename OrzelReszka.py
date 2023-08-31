<<<<<<< HEAD
import random
import time


def orzelReszka(szansaNaTrafienie): #definiowanie funkcji do losowania dwoch zmiennch
    rzut = random.uniform(0, 100)
    if (rzut < szansaNaTrafienie):
        return "Orzeł"
    else:
        return "Reszka"

print("Czy chcesz rozpocząć? Tak/Nie")

while True:

    start = input()
    start = start.capitalize()
    if start == "Tak":
        orzelReszka(50) #50% szans na wylosowanie ktorejs z odpowiedzi
    else:
        break

    print("Trwa losowanie...")

    print("3...")
    time.sleep(0.5)
    print("2...")
    time.sleep(0.5)
    print("1...")
    time.sleep(0.5)
    print(orzelReszka(50))

    print("Czy chcesz rzucić ponownie? Tak/Nie")
=======
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
>>>>>>> e25b5df25590ebde37c751bfd8df57e27d6ead9e
