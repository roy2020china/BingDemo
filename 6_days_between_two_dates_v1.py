# Given two dates, calculate how many days between the two. Account for leap days.  
# 给定两个日期，计算两个日期之间有多少天。要考虑到闰月的天数。

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    years_list = []
    for each_year in range(year1, year2):
        years_list.append(str(leap_year_or_not(each_year)))
    # boolean object is not iterable

    days_list = years_to_days(years_list)
    days = sum(days_list)
    days1 = date_to_days(year1, month1, day1)
    days2 = date_to_days(year2, month2, day2)
    days = days - days1 + days2

    # if month2 >= month1:
    #     days_difference = (m_to_d(month2)+day2) -(m_to_d(month1)+day1)
    #     days = year_to_days + days_difference
    # else:
    #     days_difference = (m_to_d(month1) + day1) -(m_to_d(month2)+day2)
    #     days = year_to_days - days_difference
    # days_difference = (m_to_d(year2, month2) + day2) - (m_to_d(year1, month1) + day1)
    # days = year_to_days + days_difference

    print days
    return days

def date_to_days(year, month, day):
    if leap_year_or_not(year):
        days_of_each_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_of_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    for i in range(0, month - 1):
        days = days + days_of_each_month[i]
    days = days + day
    return days  # how many days start from Jan 1st of that year


def leap_year_or_not(year):
    if year % 4 == 0:
        if year % 100 > 0:
            return True
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def years_to_days(years_list):
    values = []
    value = 0
    for each_year in years_list:
        #print each_year
        if each_year == "True":# NOT True
            value = int(366)
        if each_year == "False":
            value = int(365)
        values.append(value)
    return values
