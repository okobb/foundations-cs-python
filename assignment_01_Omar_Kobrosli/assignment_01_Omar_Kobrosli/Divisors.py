def findDivisors(number): 
    list = [1, ]
    if number % 2 == 0:
        number2 = number // 2
        list.append(2)
        list.append(number2)

    if number % 3 == 0:
        number2 = number // 3
        list.append(3)
        list.append(number2)

    if number % 4 == 0:
        number2 = number // 4
        list.append(4)
        list.append(number2)

    if number % 5 == 0:
        number2 = number // 5
        list.append(5)
        list.append(number2)

    if number % 6 == 0:
        number2 = number // 6
        list.append(6)
        list.append(number2)
    
    if number % 7 == 0:
        number2 = number // 7
        list.append(7)
        list.append(number2)

    if number % 8 == 0:
        number2 = number // 8
        list.append(8)
        list.append(number2)
    
    if number % 9 == 0:
        number2 = number // 9
        list.append(9)
        list.append(number2)
    
    if number % 10 == 0:
        number2 = number // 10
        list.append(10)
        list.append(number2)

    list.append(number)
    res = [*set(list)]
    res.sort()
    print(res)



findDivisors(150)
