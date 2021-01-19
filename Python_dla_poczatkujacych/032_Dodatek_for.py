#1
fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0

for digit in range(fibonacciIterations):
    print("Step:", digit, "Value:", a3)
    a1 = a2
    a2 = a3
    a3 = a1 + a2
print('-------------------------------------------------')

#2
text = '''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''
words = text.replace("\n", " ").split(" ")

for pWord in words:
    pword1 = pWord.lower().find('p')
    if pword1 >= 0:
        print(pWord)
print('-------------------------------------------------')

#3
dictionary = {'A': '80%-100%', 'B': '60%-80%', 'C': '50-60%', 'D': 'less than 50%'}

#for range in dictionary:
#    if range == "A":
#        print(range + ' ' + '-' + ' ' + dictionary['A'])
#        continue
#    elif range == "B":
#        print(range + ' ' + '-' + ' ' + dictionary['B'])
#    elif range == "C":
#        print(range + ' ' + '-' + ' ' + dictionary['C'])
#        continue
#    elif range == "D":
#        print(range + ' ' + '-' + ' ' + dictionary['D'])
#        break

for word in dictionary.keys():
    print(word, '-', dictionary[word])
print('-----------------------------------------------')

wordDictionary = {}
listOfWords = text.replace("\n", " ").split(" ")

for word in listOfWords:
    if word in wordDictionary.keys():
        wordDictionary[word] = wordDictionary[word] + 1
    else:
        wordDictionary.setdefault(word, 1)
    print(wordDictionary)
