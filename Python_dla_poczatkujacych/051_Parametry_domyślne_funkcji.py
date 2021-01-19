from datetime import date
from datetime import timedelta

def GiveWorkingDay(year=date.today().year, month=date.today().month, day=date.today().day):
    #prints the nearest working day date

    day = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("Working day for", day, "is", workingday)
    return

GiveWorkingDay(2017, 9)
GiveWorkingDay(2017,9, 2)
GiveWorkingDay(2017)
GiveWorkingDay()


# Parametry domyślne funkcji - LAB

#1

def PrintAnimal(animal=""):
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

PrintAnimal()
PrintAnimal("bear")

#2
# from datetime import date -> normalnie chcąc użyć date. jako parametr domyślny funkcji należałoby przenieść ten
# wycinek kodu powyżej funkcji; z racji tego, że wyżej już mamy ten import w tym pliku zakomentowałem tę linię

def DaysTillEndOfYear(year=date.today().year, month=date.today().month, day=date.today().day):
    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
    return

DaysTillEndOfYear()
DaysTillEndOfYear(2020, 9, 19)