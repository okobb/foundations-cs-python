
"""
def findEven():
    counter = int(input("Please enter the length of the list: "))
    number_list = []
    number_list2 = [] 
    while (counter > 0):
            choice = int(input("Your number: "))
            number_list.append(choice)
            if(choice % 2 == 0):
                number_list2.append(choice)
            counter -= 1
    if (counter == 0):
        print("Your list: ",number_list)
        print("Even numbers: ",number_list2)

findEven()
"""