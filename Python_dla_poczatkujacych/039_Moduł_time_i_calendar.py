import time

print("Currect time is ... unix epoch", time.time())
print("\n")
print("Current time is... tuple", time.localtime(time.time()))
print("\n")
print("Current time is... for human", time.asctime(time.localtime(time.time())))
print("\n")
print("Currect time is... for human", time.localtime(time.perf_counter()))
print("\n\n\n\n\n\n")

# playing with calendar

import calendar
print('---------------------------')
print(calendar.month(2017, 9 , w = 5, l = 2))
print('---------------------------')
print(calendar.month(2017, 9))
print('---------------------------')
print('week day is', calendar.weekday(2017, 9, 29))
print('---------------------------')
#calendar.setfirstweekday(6)
print('---------------------------')
print(calendar.month(2017, 9))
print('---------------------------')
print('week day is', calendar.weekday(2017, 9, 29))
print('---------------------------')
print('is 2020 a leap year?', calendar.isleap(2020))
print('---------------------------')
print('Leap days 2000 - 2017', calendar.leapdays(2000, 2017))
print('Leap days 2000 - 2020', calendar.leapdays(2000, 2020))
print('Leap days 2000 - 2021', calendar.leapdays(2000, 2021))

print(calendar.calendar(2018))

print('---------------------------')

# Moduł time i calendar - LAB

#1 moduł time zaimportowany powyżej

#2
print(time.time())

print('---------------------------')

#3
print(time.asctime(time.localtime(time.perf_counter())))

print('---------------------------')

#4 moduł calendar zaimportowany powyżej

#5
print(calendar.month(1993, 9, 19))

print('---------------------------')

#6
calendar.setfirstweekday(6)

print('---------------------------')

#7
print(calendar.month(1993, 9, 19))
print('---------------------------')

#8
print("Is year 2000 a leap year?", calendar.isleap(2000))
print('---------------------------')

#9
print(calendar.calendar(2019))
print('---------------------------')
