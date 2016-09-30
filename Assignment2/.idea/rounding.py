import math
def RoundNumToNearestMultiple(num, n):
    """

    :param num: number to round up
    :param n: number to find closest multiple of
    :return: return the closest multiple of n to num
    """
    #return num rounded to the nearest multiple of n
    #number to multiply n by to get nearest multiple

    average = num / n
    round_up = math.ceil(average)
    round_down = int(average)
    near_multiple = round_down * n if(num - (round_down * n)<(
        round_up*n)-num) else round_up*n



    print(near_multiple)
    return near_multiple


RoundNumToNearestMultiple(int(input("Please enter number to round: ")),
                          int(input("Please enter number to find closest multiple of: ")))
