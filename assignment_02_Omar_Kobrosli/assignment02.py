def main():
    """
    def menu():
        choice = int(print("1. Count Digits\n"
            + "2. Find Max\n" 
           + "3. Count Tags\n"
             + "4. Exit\n"
            + "- - - - - - - - -\n"
             + "Enter a choice:"))
        if choice == 1:
            countDigits()
        elif choice == 2:
            findMax():
        elif choice == 3:
            countTags()
        else:
            exitProgram
            
    menu()
    """
    """
    def countDigits(num):
        if num < 0 :
            return -99
        if num < 10:
            return 1
        else:
            result =  1 + countDigits(num // 10)
            return "Output: ",result
    print(countDigits(-9))
    """
    
    '''
    def findMax(list,length):
        if list == []:
            return 0
        if length == 1:
            return list[length - 1]
        else:
            num1 = findMax(list, length - 1)
            num2= list[length - 1]
            if num1 > num2:
                return num1
            else:
                return num2

    print(findMax([],0))
    '''
    """
    def countTags (code, tag):
        if (len(code) == 0 or len(code) < len(tag)):
            return 0
 
        # Recursive Case
        # Checking if the first
        # tag matches
        if (code[0 : len(tag)] == tag):
            return countTags(code[1:],tag) + 1
 
    # Otherwise, return the count
    # from the remaining index
        else:
            return countTags(code[1:],tag)
    print(countTags("<html> <head> <title>My Website</title>"
    , "<title>"))
    
    def exitProgram():
        return "Thank you for checking my program."
    """


main()
