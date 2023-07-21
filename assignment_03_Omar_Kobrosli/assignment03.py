"""
def sumTuples():
    counter = 0

    list1 = []
    counter = eval(input("Enter the length of your lists: "))
    for i in range(counter):
        num1= int(input("Enter numbers of the first list: "))
        list1.append(num1)
        
    list2 = []
    for i in range(counter):
        num2= int(input("Enter numbers of the second list: "))
        list2.append(num2)
    
    total = []
    for i in range(counter):
        sum = list1[i] + list2[i]
        total.append(sum)

    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    total1 = tuple(total)

    print("First tuple is: ",tuple1)
    print("Second tuple is: ",tuple2)
    print("Output: ",total1)
sumTuples()
"""

def exportJson(dictionary,file):
    file = open(file, "w")
    text = str(dictionary)
    text1 = text.replace("'",'"')
    file.write(text1)
    file.close()
exportJson({"year" : 2020}, "json.txt")

def importJson(file):
    file = open(file)
    text = file.read()
    
    print(text)
    file.close()
importJson("json.txt")
        