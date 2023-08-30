list_2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14]]
row_size = len(list_2)

# print(list_2[1][3]) #[row index number][colum index number]

# for row in range(row_size): #row=0, #row=1, #row=2
#     col_size = len(list_2[row]) #len(list_2[0]) = 5; #len(list_2[1]) = 5;  #len(list_2[2]) = 4
#     for col in range(col_size):
#         print(row,col)
#         print(list_2[row][col])


#how to do list comprehension for two dimension variable

for row in list_2: #row=0, #row=1, #row=2
    print(row)
    for col in row:
        print(col)