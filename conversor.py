run = True
while run:
    print('Select an option')
    option = input("1. Convert °C to °F/ 2. Convert °F to °C:   ")
    if (option=='1'):
        x = float(input("Insert a temperature °C:   "))
        convertion = ((x*9)/5) +32
        print(str(x)+'°C is '+str(convertion)+'°F')
        run= False

    elif(option=='2'):
        x = float(input("Insert a temperature °F:   "))
        convertion = ((x-32)*(5/9))
        print(str(x)+'°F is '+str(convertion)+'°C')
        run= False

    else:
        print("Try again")

