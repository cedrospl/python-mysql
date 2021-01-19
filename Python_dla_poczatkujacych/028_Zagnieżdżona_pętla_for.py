for x in range(1, 6):
    line = str(x)
    for y in range(1, 6):
        line += ('\t%3d' % (x * y))
    print(line)

# Zagnieżdżona pętla for - LAB

#1
i = 10
result = 1

for n in range(1, 11):
    result *= n
print(i, result)


print('------------')

#2
x = 10
for i in range(1, x + 1):
    result = 1
    for j in range(1, i + 1):
        result *= j
    print(i, result)


print('------------')

#3
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for rzeczownik in list_noun:
    for przymiotnik in list_adj:
        print(przymiotnik + ' ' + rzeczownik)