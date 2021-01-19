message1 = 'Processing file %s'
print(message1 % 'file_1.txt')
message2 = 'File %s has size %d KB'
print(message2 % ('file_1.txt', 100))
message3 = 'File %20s has size %10d KB'
print(message3 % ('file_1.txt', 100))
message4 = 'Processing file {0:s}'
print(message4.format('file_1.txt'))
message5 = 'File {0:s} has size {1:d}'
print(message5.format('File_1.txt', 100))
message6 = 'File {1:s} has size {0:d}'
print(message6.format(100, 'file_01.txt'))
message7 = 'File {0:20s} has size {1:10d}'
print(message7.format('File_1.txt', 100))

# Formatowanie napisów - LAB
helloMessage1 = "Hello %s!"
print(helloMessage1 % 'Kate')
print(helloMessage1 % 'Chris')
helloMessage2 = "Hello {0:s}!"
print(helloMessage2.format("Kate"))
print(helloMessage2.format("Chris"))
helloMessage3 = "%s has %d %s"
print(helloMessage3 % ("Kate", 1, "animal"))
print(helloMessage3 % ("Chris", 100000, "$"))
helloMessage4 = "{0:s} has {1:d} {2:s}"
print(helloMessage4.format("Kate", 1, "animal"))
print(helloMessage4.format("Chris", 100000, "$"))
line1 = "{0:20s} costs {1:6d} €"
print(line1.format("ICE CREAM", 3))
print(line1.format("TRIP TO VENICE", 119))
print(line1.format("PIZZA HAWAI", 6))
line2 = "{0:s} {1:d}"
print(line2.format("ICE CREAM", 3))
print(line2.format("TRIP TO VENICE", 119))
print(line2.format("PIZZA HAWAI", 6))
