import os

webaddresses = []
line = input("Please provide web address e.g. 'www.google.com' or press ENTER to stop: ")
while line != '':
    webaddresses.append(line)
    line = input("Please provide web address e.g. 'www.google.com' or press ENTER to stop: ")

print(webaddresses)
dirname = os.getcwd()
filename = input("Please provide the name for your file (without directory): ")
filepath = os.path.join(dirname, filename)
file = open(filepath, 'w+')
for address in webaddresses:
    file.write(address + '\n')
file.close()

