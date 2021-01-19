i = 1
imax = 10

while i <= imax:
    print(i, "I like Python")
    i += 2
else:
    print("Now i =", i)

i1 = 10
imax1 = 0

while i1 >= imax1:
    print(i1, "I like Python")
    i1 -= 2
else:
    print("Now i1 =", i1)

# Pętla while - LAB

#1
firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow <= lastRow:
    print("Row number", currentRow)
    currentRow += 1

#2
firstNumber = 1
lastNumber = 13

while firstNumber <= lastNumber:
    print(firstNumber, "Squared number:", firstNumber * firstNumber)
    print(firstNumber, "Cubed number:", firstNumber * firstNumber * firstNumber)
    firstNumber += 1

#3
x = 0
y = 16
z = 2 ** x
while x <= y:
    print("Two squared by", x, "=", 2 ** x)
    x += 1


#4
a = 1
b = 10

while a <= b:
    print(a * "x")
    a += 1
