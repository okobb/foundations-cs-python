def calcFactorial(number):
    counter = number
    test = number
    while counter > 1:
        
        factorial = number - 1
        total = test * factorial
        number -= 1
        test = total
        counter -= 1
        if counter == 2:
            print(total)

   

    

    
calcFactorial(100)       
