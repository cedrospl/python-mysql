persons = ['Elizabeth', 'Steven', 'Sebastian', 'Margaret', 'Svetlana', 'Raphael']

domain = 'my.company.com'

for person in persons:
    email = person + '@' + domain
    print('Email for\t', person, '\tis\t', email)
else:
    print('-- end of the list --')

# FOR - LAB

#1
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for element in data:
    print(element.upper())

print('------------')

#2
for element in data:
    elements = element.split(":")
    print(elements[0].upper())
    print(elements[1])

print('------------')

#3
for element in data:
    elements = element.split(":")
    if elements[0] == "Error":
        print(elements[1].upper())
    else:
        print(elements[1])