import random
#for i in range(32, 127):
#    print(i, chr(i))

ints = range(33, 126)
password = ''

for i in range(16):
    password += chr(random.choice(ints))
print(password)

print('-------------------------------------------------')


# Moduły - przykład - LAB

#1 moduł random zaimportowany na górze pliku

min = 1
max = 6

dice = random.randint(min, max)

if dice == 1:
    print('   ')
    print(' o ')
    print('   ')
elif dice == 2:
    print('  o')
    print('   ')
    print('o  ')
elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')

print('-------------------------------------------------')

#2

dices = []
for i in range(5):
    dices.append(random.randint(min, max))
dices.sort()
print(dices)

print('-------------------------------------------------')
