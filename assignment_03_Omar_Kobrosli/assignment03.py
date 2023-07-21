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

"""
def exportJson(dictionary,file):
    file = open(file, "w")
    #changing the dictionary into a string to be a valid JSON format
    text = str(dictionary)
    text1 = text.replace("'",'"')
    file.write(text1)
    file.close()
exportJson({
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "address": {
        "city": "New York",
        "zip": "10001"
    },
    "interests": ["reading", "traveling", "coding"]
    }, "json.txt")
"""

def importJson(file):
    file = open(file)
    text = file.read()
    # changing string into dictionary
    text = text.replace('{' , '')
    text = text.replace('}' , '')
    
    newdict = dict((a.strip(), b.strip())  
        for a, b in (element.split(':')  
            for element in text.split(', ')))
    
                

    res = {key.replace('"', ''):val for key, val in newdict.items()}
    #printing converted dictionary  
    print(res)
    print(type(res))
    file.close()
importJson("json.txt")
        