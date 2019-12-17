print("Zadanie Pierwsze")

imie = input("Wpisz pierwsza litere swojego imienia: ")
nazwisko = input("Wpisz swoje cale nazwisko: ")
print("A oto Ty: " + imie + "." + nazwisko)

print("Zadanie drugie")
imie = input("Wpisz pierwsza litere swojego imienia: ")
nazwisko = input("Wpisz swoje cale nazwisko: ")
print("A oto Ty: " + imie.upper() + "." + nazwisko.upper())

print("Zadanie trzecie")
print("Witaj!")
dwienajpierw = input("Podaj dwie pierwsze cyfr aktualnego roku: ")
dwiepozniej = input("Podaj dwie koncowe cyfry aktualnego roku: ")
wiek1 = input("A teraz podaj swoj wiek: ")
dwienajpierw += dwiepozniej
print("Uwaga uwaga... Dzieje sie magia!")
print("Aktualny rok to: " + dwienajpierw)
a = int(dwienajpierw)
b = int(wiek1)
c = a - b
print("A rok Twoich narodzin to: ", c)

