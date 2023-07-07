"""
def checkIP():
    IP = input("Enter IP address: ")
    split = IP.split(".")
    number = 0
    counter = 0
    
    if(len(split) != 4):
        print("Invalid IP address.")
    else:
        for octet in split:
            number = int(octet) 
            if (number < 0 or number > 255) or (len(octet) > 1 and octet[0] == "0"):
                print("Invalid IP addresss.")
                break
            else:
                counter += 1
            if counter == 4:
                print("Valid IP address.")

checkIP()
"""
