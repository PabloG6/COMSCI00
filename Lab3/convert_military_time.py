

military_hour = int(input("Enter the hour: "))
military_minute = int(input("Enter the minute: "))
meridian = 'AM'

'''check if the military hour is between 1 and 23 inclusive'''
if((military_hour>0) and (military_hour<=24)):

    '''if greater than or equal to 12, find the modulus and change meridian to PM'''
    if(military_hour>=12):
        standard_hour = military_hour%12
        meridian = 'PM' if(standard_hour!=0 or military_hour==12) else 'AM'
        standard_hour='12' if(standard_hour==0) else standard_hour
    else:
        standard_hour = military_hour

else:
    print("That's not the standard 24 hours! Terminating program")
    standard_hour = 0
    #end program
    quit()


if((military_minute>=0) and (military_minute<60)):
    military_minute = '0'+str(military_minute) if(military_minute<=9) else military_minute
    print(str(standard_hour) +':'+ str(military_minute), meridian)
else:
    print('That\'s not the standard 60 minutes! Terminating program')
    #end program
    quit()




