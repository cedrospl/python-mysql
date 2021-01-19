#1

def PrintAnimal(animal):
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

    if animal == 'cat':
        print(catImage)
    elif animal == 'bear':
        print(bearImage)
    elif animal == 'bat':
        print(batImage)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
    return




PrintAnimal(animal='cat')
PrintAnimal(animal='bear')
PrintAnimal(animal='bat')
PrintAnimal(animal='fish')

#2

def DaysTillEndOfYear(year, month, day):
    from datetime import date
    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
    return

DaysTillEndOfYear(2020, 11, 1)
DaysTillEndOfYear(day=30, month=1, year=3232)