"""
def reverseString():
    sentence = input("Input: ")
    counter = len(sentence)
    if counter > 0:
       for i in range(len(sentence)):
        reverse = sentence[counter - 1]
        print(reverse,end= "")
        counter -= 1


reverseString()
"""