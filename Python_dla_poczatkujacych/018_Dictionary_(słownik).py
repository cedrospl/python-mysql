CountryLeaders = {'PL':'Duda', 'US':'Trump'}

print(CountryLeaders['US'])

CountryLeaders['DE'] = 'Merkel'

#print(CountryLeaders.keys())
#print(CountryLeaders.values())
#print(CountryLeaders.items())

#print(CountryLeaders.popitem())

#print(CountryLeaders.setdefault('FR','Macron'))

#print(CountryLeaders.get('RU'))

NewLeaders = {'RU':'Putin', 'DE':'Schulz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders)

print(CountryLeaders)

# Dictionary - LAB

#1
channels = {'Google': 1480, 'Email': 300, 'Natural Traffic': 440, 'TV Spot': 700}
print(channels)
#2
print(channels['Email'])
#3
channelsUpdate = {'Natural Traffic': 520, 'News': 600}
print(channelsUpdate)
#4
channels.update(channelsUpdate)
print(channels)
#5
print(channels.keys())
#6
channels.pop('Email')
print(channels)