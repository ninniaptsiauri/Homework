# addition of 3rd, 9th and 14th elements of list

mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
sum = mylist[2] + mylist[8] + mylist[13]
print(sum)



#make a list of 20 random numbers, make new list from odd numbers and find min/max
import random

rand_list = []
rand_list = random.sample(range(1,100), 20)
print("Random list:", rand_list)
odd_list = [i for i in rand_list if i %2 != 0]
print("Only odd numbers:", odd_list)
odd_list.sort()
print("The lowest is:", odd_list[0])
print("The highest is:", odd_list[-1])
    


# find index of '210', add 'hello', remove element[2], make new list and clear

my_list = [43, '22', 12, 66, 210, ["hi"]]
print("The index of 210 is:", my_list.index(210))
my_list.append("hello")
my_list.pop(2)
print(my_list)
my_list2 = my_list.copy()
my_list2.clear()
print(my_list)
print(my_list2)



# sum of 2 matrix

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [2, 4, 6],
    [8, 9, 7],
    [5, 3, 1]
]

result = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
       row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print(result)




#transpose matrix

matrix = [
    [1, 5, 3],
    [4, 2, 6],
    [8, 7, 9]
]

transpose_matrix = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        transpose_matrix[j][i] = matrix[i][j]

print(transpose_matrix)





# matrix from random numbers

import random

matrix = [[random.randint(10,50) for _ in range(4)] for _ in range(4)]
for row in matrix:
    print(row)
