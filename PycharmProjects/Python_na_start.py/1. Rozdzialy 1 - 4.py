import string

print("Pierwsze kroki")
print("Hello world")
print("wynik dodawania 2 + 2 =", 2 + 2)

print("A teraz idziemy po zmienne")
zmiennaPierwsza = 7
zmiennaDruga = 13
print("Wynik dodawania zmiennych to:", zmiennaPierwsza + zmiennaDruga)

print("Wincyj zmiennych")
x = 7
y1 = 3.14
y2 = float(8)
z = 2j

print("x=", x, "y1=", y1, "y2=", y2, "z=", z)

print("Kolejna porcja zmiennych")
a = 9
b = 4

print(a + b, a - b, a * b, a / b, a % b, a ** b, abs(a))

print("Zadanie do zmiennych")
print("1")
q = 1
w = 2
e = float(2.5)
r = float(5.93)

print(q - w, e ** r)

print("2")
t = 4
u = 7
i = t ** u
print(i)

print("zmienne znakowe")
imie = "Jan"
nazwisko = "Kowalski"

print("Zwyciezca programu zostaje " + imie + " " + nazwisko)

pierwszaCzescImienia = "Ale"
drugaCzescImienia = "ksander"
caleImie = pierwszaCzescImienia + drugaCzescImienia
print("id=", id(pierwszaCzescImienia))

print("cale imie = " + caleImie)

pierwszaCzescImienia += drugaCzescImienia
print("id=", id(pierwszaCzescImienia))

print("cale imie = " + pierwszaCzescImienia)


dlugaZmienna = "Tworzymy cale zdanie w jednej zmiennej\'' \
               ', ktore bedzie zapisane w wielu wieszach.\
                    Wszystko dzieki zastosowaniu znaku konca linii,\
                    czyli '\'."

print(dlugaZmienna)

print("""
Kolejne
dlugie
zdanie
""")

print('''
      Podobnie 
        jak wyzej''')

slowo1 = "Abc"
print(slowo1 * 3)

slowo2 = "Abrakadabra"
print(slowo2[4])
print(slowo2[2:7])
print(slowo2[3:])
print(slowo2[:3])
print(slowo2[-3:])
print(slowo2[:-3])

slowo3 = "braZYLIA"
print(slowo3.capitalize())
print(slowo3)
