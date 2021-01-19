#1
import math

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

inputdataLength = len(inputdata)
factorableLength = len(factortable)


#print("inputdata list count:", inputdataLength)
#print("factorable list count:", factorableLength)

if inputdataLength == factorableLength:
    print("OK!")
    for inputElements in inputdata:
        inputElements
        for factorableElements in factortable:
            factorableElements
    minValue = inputElements - factorableElements * inputElements
    maxValue = inputElements + factorableElements * inputElements
    print("Minimum Value:", minValue, "Maximum value:", maxValue)
    minInteger = math.floor(minValue)
    maxInteger = math.ceil(maxValue)
    print("Minimum integer:", minInteger, "inputData list elements:", inputElements, "Maximum integer:", maxInteger)
else:
    print("inputdata and factortable need to have equal number of elements")

print('--------------------------------------------------------------------')

#2
import random

factorableLength1 = random.randint(0, 1)
for inputElements1 in inputdata:
    inputElements1
    for factorableElements1 in factortable:
        factorableElements1
minValue1 = inputElements1 - random.random() * inputElements1
maxValue1 = inputElements1 + random.random() * inputElements1
print("Minimum Value:", "Maximum value:", maxValue1)
inInteger = math.floor(minValue)
maxInteger = math.ceil(maxValue)
print("Minimum integer:", minInteger, "inputData list elements:", inputElements, "Maximum integer:", maxInteger)


print('--------------------------------------------------------------------')

#3
import datetime

print("Today is:", datetime.date.today())
print('results generated:', datetime.date.today().strftime("%Y-%m-%d"))