"""
def findDivisors(): 
    number = int(input("Please input your number: "))
    list = [1, ]
    counter = 1
    while counter < number:
        if number % counter == 0:
            remainder = number // counter
            list.append(remainder)
            list.append(counter)
        counter += 1

    list.append(number)
    res = [*set(list)]
    res.sort()
    print(res)



findDivisors()
"""