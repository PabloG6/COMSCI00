def GetIntersectionSize(range_1_min, range_1_max, range_2_min, range_2_max):
    '''
    This function should return the intersection size of the two ranges.
    Replace the line below with the correct code.
    '''
    #iterate through values in range_1
    range_1 = range_1_max - range_1_min
    range_2 = range_2_max - range_2_min
    if(range_1 != 0 and range_2 != 0 and range_1_max in
        range(range_2_min, range_2_max)):
        range_between = range_1 - range_2
        return range_between

    #range_1_min is the same as range_1_max if range_1 is zero
    elif(range_1==0 and range_1_min in range(range_1_max, range_2_max)):
        return 0
    else:
        return -1


        pass
    pass



# You don't need to change anything below this line.
range_1_min = int(input('Enter the min number for range 1: '))
range_1_max = int(input('Enter the max number for range 1: '))
range_2_min = int(input('Enter the min number for range 2: '))
range_2_max = int(input('Enter the max number for range 2: '))


intersection_size = GetIntersectionSize(
    range_1_min, range_1_max, range_2_min, range_2_max)
print('The intersection size is', intersection_size)
