def leap_year_or_not(year):
    if year % 4 == 0:
        if year % 100 > 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


def days_in_month(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        if leap_year_or_not(year):
            return 29
        else:
            return 28
    else:  # (4, 6, 9, 11):
        return 30


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < days_in_month(month, year):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert month1 in range(1, 13) and month2 in range(1, 13), " the value of month should be between 1 - 12"
    # assert day1 < days_in_month(month1, year1), "the value of day in %d should be <= %d" % month1 % days_in_month(month1, year1)  # zb
    # assert day2 < days_in_month(month2, year2), "the value of day in %d should be <= %d" % month2 % days_in_month(month2, year2)  # zb
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1), \
        "year1-month1-day1 should be earlier than year2-mont2-day2!"
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
