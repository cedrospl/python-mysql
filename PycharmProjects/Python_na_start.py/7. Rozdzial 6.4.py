import sys

print("Witaj w prostym kalkulatorze!")
a = int(input("Podaj pierwsza liczbe calkowita: "))
b = int(input("Podaj druga liczbe calkowita: "))
if b == 0:
    print("Nie wolno dzielic przez zero!")
    sys.exit()

wynik = a / b
c = input("Jesli chcesz otrzymac tylko liczbe calkowita, wybierz 1, przeciwnie wybierz 2: ")

if c == '1':
    print(int(wynik))
elif c == '2':
    print(float(wynik))
#Ostatnie zadanie nie jest ruszone!
