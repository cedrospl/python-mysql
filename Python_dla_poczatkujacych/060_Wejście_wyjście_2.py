import os

filename = input("Please provide path to the file: ")
while not os.path.isfile(filename):
    print("File does not exist. Try again.")
    filename = input("Please provide good path to the file: ")

webaddresses = []

with open(filename, 'r') as file:
    for line in file:
        line = line.replace("\n", "")
        webaddresses.append(line)

for line in webaddresses:
    if line.endswith('.pl'):
        print("adres", line, "jest adresem z Polski")
    else:
        print("adres", line, "nie jest adresem z Polski")
