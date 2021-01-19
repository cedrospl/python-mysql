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

dirname = os.path.dirname(filename)

websPathPL = os.path.join(dirname, 'webs_pl.txt')
websPathOther = os.path.join(dirname, 'webs_other.txt')
filePL = open(websPathPL, 'w')
fileOther = open(websPathOther, 'w')
for line in webaddresses:
    if line.endswith('.pl'):
        print("adres", line, "jest adresem z Polski")
        filePL.write(line + "\n")
    else:
        print("adres", line, "nie jest adresem z Polski")
        fileOther.write(line + "\n")
filePL.close()
fileOther.close()