def PrintMultiples(start, end, multiple):

    print(end='\n')
    multiple_exist = False
    if(multiple<=0):
        print(">>> Input Multiples must be greater than 0")
        return
    #
    if(end>start):
        for number in range(start, end+1):
            if(number%multiple==0):
                print('>>>', number)
                multiple_exist = True
            elif(number==end and not multiple_exist):
                print('There are no multiples of', multiple, 'between the range of', start, 'to', end)
    else:
        for number in range(end, start+1):
            if(number%multiple==0):
                print('>>>',number)
                multiple_exist = True
            elif(number==start and not multiple_exist):
                print('>>> There are no multiples of', multiple, 'between the range of', start, 'to', end)
PrintMultiples(4, 10, 2)
PrintMultiples(7, -7, 3)
PrintMultiples(7, 10, 6)
PrintMultiples(-6, -6, 1)
PrintMultiples(1, 5, 0)