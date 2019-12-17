print("Witaj w prostym kalkulatorze")
a = int(input("Podaj pierwsza liczbe calkowita: "))
b = int(input("Podaj druga liczbe calkowita: "))
c = int(input("Wybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie: "))
if (c == 1):
    wynik = a + b
elif (c == 2):
    wynik = a - b
elif (c == 3):
    wynik = a * b
elif (c == 4):
    wynik = a / b
else:
    print("Dokonales zlego wyboru!")

print ("wynik dzialania to: ", wynik)
