def main():
    #def menu():
        #choice = int(print("1. Count Digits\n"
        #    + "3. Count Tags\n"
        #      + "4. Exit\n"
        #     + "- - - - - - - - -\n"
        #     + "Enter a choice:"))
    #menu()

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

    def countTags (code, tag):
        split = code.split()
        code = split
        list = []
        if len(split) != 0:
          if tag in code:
            list.append(tag) 
            split.pop(0)
            print(split)
            return countTags(code,tag)
          else:
            return countTags(code,tag)
    print(countTags("hi im omar hi how ru hi", "hi"))



main()
