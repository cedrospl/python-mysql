print("Zadanie drugie:")

def wyswietlaniecalosci(nazwa):
    print(nazwa)
    return

def zbieraniedanychosobowych(imie, nazwisko):
    return wyswietlaniecalosci(imie + " " + nazwisko)

imie = input("Podaj swoje imie: ")
nazwisko = input("Podaj swoje nazwisko: ")
zbieraniedanychosobowych(imie, nazwisko)
