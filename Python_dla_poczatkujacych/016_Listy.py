import copy

countries = ['FR', 'USA', 'DE', 'RU']
countries[1] = 'GB'
print(countries[1])
countries.append('PL')
countries.insert(2, 'ES')
countries.remove('RU')
countries.sort()
countries.reverse()
print(countries.pop(2))
print(countries.index('PL'))
#print(countries.index('US'))
print(countries.count('DE'))

newList = ['FI', 'SE']
countries.extend(newList)

countriesCopy = countries.copy()
countriesCopy.clear()

print(countries)
print(countriesCopy)

# Listy - LAB

hitsTitles = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM', 'WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
print(hitsTitles)
hitsTitles.insert(2, 'HOTEL CALIFORNIA')
print(hitsTitles)
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles)
print('HOTEL CALIFORNIA on place:', hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove('HOTEL CALIFORNIA')
print(hitsTitles)
hitsTitles[0] = 'ENJOY THE SILENCE'
print(hitsTitles)
hitsToRead = hitsTitles.copy()
print(hitsToRead)
hitsToRead.reverse()
print(hitsToRead)
hitsToRead.sort()
print(hitsToRead)
print(hitsToRead.pop(0))
print(hitsToRead)
print(hitsToRead.pop(0))
print(hitsToRead)
additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead)
print("Wish you were here played:", hitsToRead.count('WISH YOU WERE HERE'), "times")
print("Riders on the storm played:", hitsToRead.count('RIDERS ON THE STORM'), "times")
print(hitsToRead.clear())
