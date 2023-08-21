name = input("enter your name:")
email = input("enter your email:")

size_name = len(name)
size_email = len(email)
if size_name == 0 or size_email==0:
    print("the field can not be empty")
else:
    print("success")