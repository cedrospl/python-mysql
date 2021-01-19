file = open("/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/results.txt", "r")

content = file.read()
print(content)

file.close()

print("----------------------------")

#niewydajne jeśli plik jest duży
with open("/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/results.txt", "r") as file:
    content = file.read()
    print(content)

print("----------------------------")

#wydajny jeśli plik jest duży
with open("/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/results.txt", "r") as file:
    for line in file:
        print(line)

print("----------------------------")

#przykład jak się nie powinno pisać kodu (pętla + metoda .readlines - za dużo)
file = open("/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/results.txt", "r")
for line in file.readlines():
    print(line)
file.close()

print("----------------------------")

file = open("/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/results.txt", "r")

fragment = file.read(10)
while fragment:
    print(file.tell(), fragment)
    fragment = file.read(10)

file.close()

print("----------------------------")

#Odczyt danych z pliku - LAB

file_path = "/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/orders.csv"
with open(file_path, "r") as file:
    for line in file:
        line = line.replace("\n", "")
        order = line.split(",")
        if len(order) == 3:
            print("Order from drugstore '%s', item '%s', amount '%s'" %(order[0], order[1], order[2]))
        else:
            print("Line '%s' is malformed!!!" %(line))
    oprint("Processing of the file has been ended sucessfully")