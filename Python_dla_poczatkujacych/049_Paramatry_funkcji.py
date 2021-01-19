def GiveWorkingDay(year, month, day):
    #prints the nearest working day date
    from datetime import date
    from datetime import timedelta

    #day = date.today()
    day = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("Working day for", day, "is", workingday)
    return

GiveWorkingDay(2017, 9, 30)
GiveWorkingDay(2017, 10, 1)
GiveWorkingDay(2017, 10, 2)
GiveWorkingDay(2017, 10, 3)
GiveWorkingDay(2017, 10, 4)
GiveWorkingDay(2017, 10, 5)
GiveWorkingDay(2017, 10, 6)
GiveWorkingDay(2017, 10, 7)
GiveWorkingDay(year=2017, month=12, day=6)
GiveWorkingDay(day=6, month=12, year=2018)

