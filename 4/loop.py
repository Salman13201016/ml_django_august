#start = 0--------------step = +1----------------end (5)

list1 = [1,2,3,4,5,6] #list index starts from zero
# print(list1[2])

# for i in range(len(list1)): #i also starts from zero as default setting
#                             #list iteration using loop
#     print(i,list1[i])



#without index number

# for i in list1: #i also starts from zero as default setting
#                             #list iteration using loop
#     print(i)

list1 = [100,200,300,400,500,600]
list2 = ["a","b","c","d","e"]

#how enumerate function works
#how zip function function works internally
#what happens if size of any list is not equal to each other in zip
#execution time of list comprehension and tradition approach
#memory size of each index in a list according to different type of data

#list comprehension
list3 = [x-(x*.05) if x>200 else x for x in list1 ]
 
list4 = []

for x in list1:
    if(x>200):
        y = x-(x*0.05)
        list4.append(y)
    else:
        y=x 
        list4.append(y)

print(list3)

print(list4)
