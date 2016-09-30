from _datetime import datetime


# ignore this function

#
def zodiac_signs(start_date, end_date, zodiac, date):
    """
    :param start_date: start of the zodiac sign
    :param end_date: end of the zodiac sign
    :param zodiac: the name of the zodiac
    :return: tuple of zodiac
    """
    start_date = datetime.strptime(start_date, '%B %d') if(zodiac!='capricorn') \
        else datetime.strptime(start_date, '%B %d %Y')
    end_date = datetime.strptime(end_date, '%B %d')
    if(start_date<date<end_date):
        return zodiac
    else:
        return False




def compare_zodiac(date, zodiac):
    """
    :param date: date to check
    :param zodiac: zodiac tuple
    :return: return zodiac name if true
    """
    if(zodiac[0]<date<zodiac[1]):
        return zodiac[2]
    else:
        return False
    pass


def GetZodiacSign(birth_month, birth_day):
    # construct a dictionary object

    #value to return from function when for loop is complete
    return_val = str
    birth_day = format(birth_day, '02d')

    # get a birth date object
    birth_date = datetime.strptime(birth_month + ' ' + str(birth_day), '%B %d')

    # create a series of zodiac tuples
    aries = zodiac_signs('March 21', 'April 19', 'aries', birth_date)
    taurus = zodiac_signs('April 20', 'May 20', 'taurus', birth_date)
    gemini = zodiac_signs('May 21', 'June 20', 'gemini', birth_date)
    cancer = zodiac_signs('June 21', 'July 22', 'cancer', birth_date)
    leo = zodiac_signs('July 23', 'August 22', 'leo', birth_date)
    virgo = zodiac_signs('August 23', 'September 22', 'virgo', birth_date)
    libra = zodiac_signs('September 22', 'October 22', 'libra', birth_date)
    scorpio = zodiac_signs('October 23', 'November 21', 'scorpio', birth_date)
    sagittarius= zodiac_signs('November 22', 'December 21', 'sagittarius', birth_date)
    capricorn = zodiac_signs('December 22 1899', 'January 19', 'capricorn', birth_date)
    aquarius = zodiac_signs('January 20', 'February 18', 'aquarius', birth_date)
    pisces = zodiac_signs('February 19', 'March 20', 'pisces', birth_date)

    if type(aries) is str:
        return aries
    elif type(taurus) is str:
        return taurus
    elif type(gemini) is str:
        return gemini
    elif type(cancer) is str:
        return cancer
    elif type(leo) is str:
        return cancer
    elif type(virgo) is str:
        return virgo
    elif type(libra) is str:
        return libra
    elif type(scorpio) is str:
        return scorpio
    elif type(sagittarius) is str:
        return sagittarius
    elif type(capricorn) is str:
        return capricorn
    elif type(aquarius) is str:
        return aquarius
    elif type(pisces) is str:
        return pisces
    else:
        return "You're nothing"

    if type(capricorn) is str:
        return capricorn
    else:
        return "Nothing"




print(GetZodiacSign(input("Please enter your birth month: "), int(input("Please enter your birthdate: "))))
