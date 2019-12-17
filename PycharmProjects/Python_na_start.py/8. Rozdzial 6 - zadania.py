print("Zadanie 1 i 2:")
import math
import sys

print("Witaj w prostym kalkulatorze")
a = int(input("Podaj pierwsza liczbe calkowita: "))
b = int(input("Podaj druga liczbe calkowita: "))
c = int(input("Wybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie,/"
              "5 - potegowanie, 6 - pierwiastkowanie (pierwiastek kwadratowy liczby 'a': "))
if (c == 1):
    wynik = a + b
elif (c == 2):
    wynik = a - b
elif (c == 3):
    wynik = a * b
elif (c == 4):
    if b == 0:
        print("Nie wolno dzielic przez zero!")
    wynik = a / b
elif (c == 5):
    wynik = a ** b
elif (c == 6):
    wynik = math.sqrt(a)
else:
    print("Dokonales zlego wyboru!")

print("wynik dzialania to: ", wynik)


print("Zadanie 3:")
print("Porownywanie liczb")
a = int(input("Podaj pierwsza liczbe (mniejsza): "))
b = int(input("Podaj druga liczbe (wieksza): "))
if a < b:
    wynik1 = b / a
else:
    print("Podaj najpierw liczbe mniejsza a pozniej wieksza!")
print("A oto dzielenie liczby wiekszej przez mniejsza: ", wynik1)


