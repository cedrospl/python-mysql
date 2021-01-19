import os
import sys

line = input("What is the acceptable price (in EUR) for udemy course for you to buy?")
filePath = input("Please provide a path to the file: ")


try:
    file = open(filePath, 'w+')
    file.write(line + "\n")
    value = int(line)
    file.close()
    print("The value saved in the file is:", value)
except FileNotFoundError as e:
    print("Error opening file:", filePath, e)
    print("SORRY - WE HAVE AN ERROR")
except ValueError as e:
    print("The value entered cannot be converted to a number", line, e)
else:
    print("Actions completed successfully!")
