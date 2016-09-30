
def PrintPrimeFactors(num):
    # iterate through the number passed
    prime_factors_list = []
    i = 2
    if(num<=1):
        print("There are no prime factors for {}".format(num))
        pass
        # check if number isPrime
    while i <=num and num != 1:
        while isPrime(i) and num%i == 0 and num!=1:
            num = int(num/i)
            prime_factors_list.append(i)
        i+=1
    for index, item in enumerate(prime_factors_list):
        prime_factors = ''
        if index==len(prime_factors_list)-1:
            print(item)
        else:
            print(item, '*', end=' ')

            pass
        pass

    return prime_factors_list




def isPrime(num):
    i = 2
    if num == 2:
        return True
    while i<num:
        if num%i==0:
            return False
        i+=1

    return True


PrintPrimeFactors(24)
PrintPrimeFactors(1650)
PrintPrimeFactors(40378)
PrintPrimeFactors(11)
PrintPrimeFactors(1)
