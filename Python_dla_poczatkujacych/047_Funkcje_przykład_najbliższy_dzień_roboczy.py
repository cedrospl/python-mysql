def GiveWorkingDay():
    from datetime import date
    from datetime import timedelta

    #day = date.today()
    day = date(2017,9,30)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("Working day for", day, "is", workingday)
    return

GiveWorkingDay()