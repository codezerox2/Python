def Is_Even(num):
    if num % 2 == 0 and num != 0: # remove and if isnot required
        print("its even number")
    else:
        print('its not even number')

number = int(input("input the number: "))

Is_Even(number)