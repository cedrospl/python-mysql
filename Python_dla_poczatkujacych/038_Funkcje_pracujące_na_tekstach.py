line = 'this IS a very STRANGE text'
print(line.capitalize())
print(line.title())
print(line.upper())
print(line.lower())
print(line.swapcase())
print(line.casefold())
line1 = 'der Fluß'
print(line1.lower())
print(line1.casefold())
line2 = 'ŻÓŁĆ'
print(line2.lower())
print(line2.casefold())
print(line2.replace('Ż', 'Z').replace('Ó', 'O').replace('Ł', 'L').replace('Ć', 'C').lower())
print(line.count('e'))
print(line.find('e'))
print(line.rfind('e'))
print(line.index('e'))
print(line.rindex('e'))
print(line.find('p'))
#print(line.rindex('p'))
print('e' in line)
print('p' in line)
print(line.startswith('this'))
print(line.endswith('THIS'))
line3 = '''this is a long text
that spans multiple lines
but should be somehow presented in python'''
print(line3)
print(line3.count('\n'))
import string
print(string.ascii_letters)
print(string.digits)
line4 = 'this is the end of this lesson'
print(line4.split(' '))
list = line4.split(' ')
#print(list.join(' ')) - nie zadziała bo lista sama w sobie nie ma separatorów!! JOIN jest specyficzną funkcją
# wywoływaną dla napisaów!
print(' '.join(list))

print('-------------------------------------------------')

# Funkcje pracujące na tekstach - interpretacja wiersza - LAB

poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2. O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp nam legną w prochu i pyle! '''

lines = poem.split('\n')
newPoem = []
a = 0
b = 8

#moje rozwiązanie:
for truth in lines:
    if a <= 8 and b < 16:
        newPoem.append(lines[a])
        newPoem.append(lines[b])
        a += 1
        b += 1
print('\n'.join(newPoem))

#krótsze rozwiązanie:
#for i in range(8):
#    print(lines[i])
#    print(lines[i+8])

print('-------------------------------------------------')