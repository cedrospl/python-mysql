import random

print("One random number:", random.randint(1, 100)) # 1 <= N <= 100
print("\n")

print("Choosing random number from a range", random.choice(range(1, 100)))
print("\n")

print("Choosing random number from a range - easier", random.randrange(1, 100))
print("\n")

list = ['John', 'Ann', 'Peter', 'Susan', 'Emily', 'Greg', 'Chris']
random.shuffle(list)
print("Reordered list:", list)
print("\n")

print("Just a random float", random.random())
print("\n")

print('-------------------------------------------------')

# Moduł random - LAB

#1 import modułu random na górze pliku

#2
for numbers in range(10):
    print(random.randint(1, 100))

print('-------------------------------------------------')

#3

number1 = random.randint(1, 100)
print("The first generated number is:", number1)

counter = 1
number2 = random.randint(1, 100)

while number1 != number2:
        counter += 1
        number2 = random.randint(1, 100)
        print(counter, number2)
print("Attempts needed to generate %d" %(counter))

print('-------------------------------------------------')

#4
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
groupNumber = 0
numberOfCountries = len(countries)

for country in range(numberOfCountries):
    if country % 4 == 0:
        groupNumber += 1
        print("----Grupa X----")
    print(countries[country])

print('-------------------------------------------------')
