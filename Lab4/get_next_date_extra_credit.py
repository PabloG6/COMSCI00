from datetime import datetime
from datetime import timedelta
'''the formatting on the lab is off GetNextDate(day, month, year, num_days_forward)
would not return 9/17/2016 if GetNextDate(2, 28, 2004) is passed because
28 is not a month.
'''
def GetNextDate(day, month, year, num_days_forward):
    num_days_forward = int(num_days_forward) if (type(num_days_forward) == str) else num_days_forward
    day = str(day).zfill(2)
    month = str(month).zfill(2)
    year = str(year).zfill(2)
    date = '{0}/{1}/{2}'.format(day, month, year)
    new_date = datetime.strptime(date, '%d/%m/%Y')
    new_date += timedelta(days=num_days_forward)
    new_date = new_date.strftime('%m/%d/%Y')
    return new_date

print(GetNextDate(input("Please enter the day: "), input("Please enter the month: "),
                   input("Please enter the year: "), input("Enter number of days forward: ")))

