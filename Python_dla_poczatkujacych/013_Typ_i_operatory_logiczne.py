isWeekend = True
print("Is weekend =", isWeekend)

temperature = 25
print("Temperature =", temperature)

toDoList = ''
print("To Do List =", toDoList)

isHappy = isWeekend and temperature >= 20 and toDoList == ''
print("Is Happy =", isHappy)

isHappy = not isWeekend and temperature < 20 and toDoList != ''
print("Is Happy =", isHappy)

isHappy = isWeekend and temperature >= 20 and toDoList == '' \
    or not isWeekend and not (temperature >= 20 or toDoList == '')
print("Is Happy =", isHappy)

# Typ i operatory logiczne - LAB
# is the light switch in AUTOMATIC mode
isAutomaticMode = False
print("Automatic Mode:", isAutomaticMode)
# is the level of day light above 80%
is80PercentLight = True
print("Is the light good:", is80PercentLight)
# is the Sun lightinig directly into the driver's face
isDirectLight = False
print("Is sun low:", isDirectLight)
# is it rainy, foggy or other weather conditions are present
isRainy = True
print("Is it rainy:", isRainy)
turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
print("TURN LIGHTS ON:", turnLightsOn)
