from datetime import datetime
def GetDayOfYear(month, day):
    '''

    :param month: the month to be passed as a string
    :param day: the month to be passed as an integer
    :return:
    '''
    new_years = datetime.strptime('January 1', '%B %d')
    date = month+' '+str(day)
    date = datetime.strptime(date, '%B %d')
    day_of_year = date.timetuple().tm_yday
    return str(day_of_year)


print(GetDayOfYear(input("Enter month: "), int(input("Enter day: "))))
