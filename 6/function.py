#built-in function, #user-defined function, #lamda function

# print(len("salman"))
#send parameter/receiver parameter, execute logic and return the result
# count = 0

def custom_len(n=""):
    global count
    count = 0
    # count = 0
    # global count
    #local variable
    # print(n)
    for i in n:
        count = count+1
    # print(count)    #no return

    # return count

name="salman"
custom_len(name)
print(count)
