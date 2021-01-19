def DoAction(action, parameter):
    print("action", action)
    print("parameter", parameter)
    return

DoAction('buy', 'shoes')

def DoAction2(action, *parameter):
    print("action", action)
    print("parameter", parameter)
    for element in parameter:
        print("element is", element)
    return

DoAction2('buy', 'shoes', 'socks', 't-shirt')

def DoAction3(action, what, **parameter):
    print("action", action)
    print("what", what)
    print("parameter", parameter)
    for element in parameter:
        print(element, '=', parameter[element])
    return

DoAction3('buy', 'shoes', size=45, color='brown', type='sport')

# Funkcje - zmienna ilość parametrów - LAB

#1

def PrintAnimal(*animals):
    # this function prints a cat ascii-art
    catImage = r'''
|\---/|
| o_o |
 \_^_/'''

    # this function prints a bear ascii-art
    bearImage = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''

    # this function prints a bat ascii-art
    batImage = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
    for animal in animals:
        if animal == 'cat':
            print(catImage)
        elif animal == 'bear':
            print(bearImage)
        elif animal == 'bat':
            print(batImage)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
    return

print(PrintAnimal('bear', 'fish', 'bat', 'snail'))

#2
from datetime import date

def DaysTillEndOfYear(*dates):
    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print("Date", date_today, "days till the end of year:", delta.days)


DaysTillEndOfYear(date(2020, 9, 3))
DaysTillEndOfYear(date(1993, 9, 19), date(2007, 4, 30), date(2010, 10, 10))