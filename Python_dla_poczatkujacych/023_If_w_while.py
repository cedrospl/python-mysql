values = [10, 43, 12, 48, 12, 11, 18, 98, 57, 28, 19, 27, 49, 19, 74]

i = 0
max = len(values) - 2

while i < max:
    print(i, values[i], values[i + 1], values[i + 2])

    if values[i] < values[i + 1] and values[i + 1] < values[i + 2]:
        print('\tFound: ',values[i], values[i + 1], values[i + 2])

    i += 1

# If w while - przykład: wyszukiwanie wzorca - LAB

#1
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

x = 0
max1 = len(numbers) - 1

while x < max1:
    print(x, numbers[x], numbers[x + 1])

    if numbers[x] * numbers[x] == numbers[x + 1]:
        print("\t\tFound!")
    x += 1

#2
numbers1 = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

x1 = 0
max2 = len(numbers1) - 2

while x1 < max2:
    print(x, numbers1[x1], numbers1[x1 + 1], numbers1[x1 + 2])

    if numbers1[x1] * numbers1[x1] == numbers1[x1 + 1] and numbers1[x1 + 1] * numbers1[x1 + 1] == numbers1[x1 + 2]:
        print("\t\tFound!")

    x1 += 1

#3
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

a = 0
maximum = len(texts) - 1

while a < maximum:
    print(a, texts[a], texts[a + 1])

    if len(texts[a]) == len (texts[a + 1]):
        print("\t\tFound!")

    a += 1
