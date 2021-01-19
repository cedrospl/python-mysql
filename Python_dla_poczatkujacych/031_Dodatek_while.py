#1
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year = 0
capital = initialCapital

while year < maxTimeYears:
    year += 1
    capital = round((1 + percent) * capital, 2)
    print('after year:', year,  'you will have:', capital)
else:
    print('the total revenue is', capital-initialCapital)
print('-------------------------------------------------------')

#2
number = 20730906
variable = number
sumOfDigits = 0

while variable > 0:
    lastNumber = variable % 10
    sumOfDigits += lastNumber
    variable = variable // 10
else:
    print("The sum of digits of", number, sumOfDigits)
print('-------------------------------------------------------')

#3
text = "United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier."
wordLength = 6
listOfWords = text.split(" ")
shortWords = 0
longWords = 0
a = 0

while listOfWords:
    word = listOfWords[a]
    if len(word) > wordLength:
        longWords += 1
    else:
        shortWords += 1
    a += 1
    print("Number of short words: ", shortWords)
    print("Number of long words: ", longWords)
