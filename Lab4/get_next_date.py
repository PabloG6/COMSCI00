from datetime import datetime
from datetime import timedelta
'''the formatting on the lab is off GetNextDate(day, month, year)
would not return 9/17/2016 if GetNextDate(9, 16, 2016) is passed because
16 is not a month.
'''
def GetNextDate(day, month, year):
    '''

    :param day: day to pass
    :param month: month to pass
    :param year: year to pass
    :return: new_date as string
    '''
    day = str(day).zfill(2)
    month = str(month).zfill(2)
    year = str(year).zfill(2)
    date = '{0}/{1}/{2}'.format(month, day, year)
    new_date = datetime.strptime(date, '%m/%d/%Y')
    new_date += timedelta(days=1)
    new_date = new_date.strftime('%m/%d/%Y')
    return str(new_date)


print(GetNextDate(input("Please enter the day: "), input("Please enter the month: "),
                  input("Please enter the year: ")))

