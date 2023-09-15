def acces_age(year_of_birth):
    min_age = 18
    actually_year = 2023
    if min_age <= actually_year - year_of_birth:
        print("You are adult")
    else:
        print("You are not adult")

acces_age()

