name = input("enter your name:")

email = input("enter your email:")
phone = input("enter your phone: ")

size_name = len(name)
size_email = len(email)
size_phone  = len(phone)
if size_name == 0 or size_email==0 or size_phone==0:

    print("the field can not be empty")
else:
    #OV x = 1 and y = 9 || x and y = 0
    if(size_name<3 or size_name>10): #nested condition
        print("the name length must be minimum 3")
    elif(size_phone!=11):
        print("the phone number must have 11 digits")
    else:
        print("success")