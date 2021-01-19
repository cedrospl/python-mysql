for number in range(1, 21):
    if number % 2 == 0:
        print('Number %2d is %s' % (number, 'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))

print('vvvvvvvvvvvvvvvvvvvvv')

# Pętla wykonywana określoną ilość razy - LAB

#1
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for wzorek in range (10):
    print(string_A)

print('vvvvvvvvvvvvvvvvvvvvv')

for wzorek in range (9):
    if wzorek % 2 == 0:
        print(string_A)
    else:
        print(string_B)

print('vvvvvvvvvvvvvvvvvvvvv')

#2
sign1 = "x"
sign2 = "o"
for iksy in range (1, 10):
    print(sign1 * iksy)

print('vvvvvvvvvvvvvvvvvvvvv')

for iksyIkółka in range (1, 10):
    if iksyIkółka % 2 == 0:
        print(sign1 * iksyIkółka)
    else:
        print(sign2 * iksyIkółka)

print('vvvvvvvvvvvvvvvvvvvvv')