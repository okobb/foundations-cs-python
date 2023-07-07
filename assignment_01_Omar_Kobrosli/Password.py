"""
def checkPassword():
    password = input("Please enter your password: ")

    special = password
    special.split()
    counter = 0
    s = '!?#$'  
    for i in range(len(special)):
        if special[i] in s:
            counter += 1
            specialc = True
        else:
            specialc = False

    if password.islower() == False:
        upper = True
    else:
        upper = False
    if password.isupper() == True:
        upper = False

    num = False
    let = False

    for i in password:
     
        if i in "abcdefghijklmnopqrstuvwxyz":
            num = True

 
        if i in "0123456789":
            let = True

    if let == True and num == True:
        alphanum = True
    else:
        alphanum = False

    length = False
    if len(password) >= 8:
        length = True


    
    
    if upper == True and alphanum == True and length == True and specialc == True:
        print("Strong Password.")
    else:
        print("Weak Password.")  
  
checkPassword()
"""