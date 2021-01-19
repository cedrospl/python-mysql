age = 22
isDrunk = True
isRestrictedArea = False

if age < 18:
    print("You are too young to buy alcohol")
else:
    if isDrunk:
        print("Are you drunk? We cannot sell you alcohol")
    else:
        if isRestrictedArea:
            print("Restricted area. Alcohol is forbidden")
        else:
            print("OK, you can buy alcohol")

print ("----")

if age < 18:
    print("You are too young to buy alcohol")
elif isDrunk:
    print("Are you drunk? We cannot sell you alcohol")
elif isRestrictedArea:
    print ("Restricted area. Alcohol is forbidden")
else:
    print("OK, you can buy alcohol")

# Instrukcja if/elif - LAB

#1
minLikes = 500
minShares = 100
numLikes = 550
numShares = 110

if numLikes >= minLikes and numShares >= minShares:
    print("Discount -10% acquired!")
elif numLikes < minLikes:
    print("Sorry, no discount has been acquired because minimum number of Likes is 500!")
elif numShares < minShares:
    print("Sorry, no discount has been acquired because minimum number of Shares is 100!")
else:
    print("Sorry, no discount has been acquired")

#2
isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Your Burger coupon is: XXXXXXX")
elif not isPizzaOrdered or isBigDrinkOrdered:
    print("You need to order a pizza or a big soda to get a burger coupon!")
elif isWeekend:
    print("Order needs to be made outside the weekends to get a burger coupon!")
else:
    print("Buy more to get a burger coupon!")