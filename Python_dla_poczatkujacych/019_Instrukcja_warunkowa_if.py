age = 27

if age >= 18:
    print("You are an adult and can buy alcohol")
else:
    print("You are too young to buy alcohol")

isDrunk = False

if age >= 18 and not isDrunk:
    print("You are an adult and can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")

isRestrictedArea = False

if age >= 18 and not isDrunk and not isRestrictedArea:
    print("You are an adult and can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")

# Instrukcja warunkowa IF - LAB

#1
minLikes = 500
minShares = 100
numLikes = 550
numShares = 111

if numLikes >= minLikes and numShares >= minShares:
    print("Discount -10% acquired!")
else:
    print("Sorry, no discount has been acquired")

#2
isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Your Burger coupon is: XXXXXXX")
else:
    print("Buy more to get a burger coupon!")

#3
diskSize = 140
diskSizeUsed = 123
fileSize = 10

if (diskSize - diskSizeUsed) >= fileSize:
    print("The file can be downloaded")
else:
    print("No space on your disk to download this file")