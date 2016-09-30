def CountPrimeNumbers(num):
    number_of_prime = 0
    #iterate through the loop
    for item in num:
        if item == 2:
            number_of_prime+=1
        for divisor in range(2, item):
            if item % divisor == 0:
                break
            elif divisor == item - 1:
                number_of_prime += 1


    pass
    return number_of_prime


print("answer:", CountPrimeNumbers([4, 7, 8, 11, 17]))
print("answer:", CountPrimeNumbers([27281, 23547, 23549, 23551, 41661]))
print("answer:", CountPrimeNumbers([-3, -2, -1, 0, 1, 2, 3]))
print("answer:", CountPrimeNumbers([]))