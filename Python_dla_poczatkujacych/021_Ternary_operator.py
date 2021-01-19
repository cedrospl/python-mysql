itRains = True

if itRains:
    print("We stay at home")
else:
    print("We go out")

print("We stay at home" if itRains else "We go out")

# IF - LAB

#1
musclePain = False
fever = False
weakness = False

#2
if musclePain and fever and weakness:
    print("Suspicion of influenza")
else:
    print("The flu is unlikely")

#3
if musclePain and fever and weakness:
    print("Suspicion of influenza")
elif weakness and not fever or not musclePain:
    print("Just take a rest!")
else:
    print("You may be cold")

#4
isMan = True

#5
if musclePain and fever and weakness or musclePain and isMan or fever and isMan or weakness and isMan:
    print("Suspicion of influenza")
elif weakness and not fever or not musclePain:
    print("Just take a rest!")
else:
    print("You may be cold")

#6
isCheckCompleted = True

print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")
