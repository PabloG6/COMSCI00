num_1 = input('Enter the 1st number: ')
num_2 = input('Enter the 2nd number: ')
num_3 = input('Enter the 3rd number: ')

if((num_1>num_2 and num_1<num_3) or (num_1<num_2 and num_1>num_3)):
    print('The middle number is ', num_1)
elif((num_2>num_1 and num_2<num_3) or (num_2<num_1 and num_2>num_3)):
    print('The middle number is', num_2)
elif((num_3>num_1 and num_3<num_2) or (num_3<num_1 and num_3>num_2)):
    print('The middle number is', num_3)
else:
    print('This project has no median')


