import calendar

def number_of_days(year, month):
    '''
        year: positive integer
        month: positive integer
        return: the number of calendar days in a given year and month
    '''
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert year > 0 and month > 0 and month <= 12

    return calendar.monthrange(year,month)[1]

def number_of_leap_years(year1, year2):
    '''
        year1: positive integer
        year2: positive integer
        return: the number of leap-years between two given years
    '''
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    assert year1 > 0 and year2 > 0

    return len([y for y in range(year1, year2 + 1) if calendar.isleap(y)])

def get_day_of_week(year, month, day):
    '''
        year: positive integer
        month: positive integer
        day: positive integer
    '''
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert isinstance(day, int)

    assert year > 0 and month > 0 and month <= 12
    assert day > 0 and day <= number_of_days(year, month)

    return calendar.day_name[calendar.weekday(year, month, day)]
