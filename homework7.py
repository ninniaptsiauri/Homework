# number 1

squared_members = {i**2 for i in range(1,11)}
print(squared_members)



# number 2 

txt = input("Please enter a text: ")
set1 = set(txt)
print(set1)



# number 3 

tuple1 = (4, 89, "hello", 54, "Python", 60, 113)
tuple2 = (60, 78, 10, 'Python', 'sky', 54, 100, 60)
compined_tuples = ()
duplicated_values = []
for i in tuple1:
    if i not in tuple2:
        compined_tuples += (i,)
        for j in tuple2:
            if j not in compined_tuples:
                compined_tuples += (j,)
print(compined_tuples)


tuple1 = (4, 89, "hello", 54, "Python", 60, 113)
tuple2 = (60, 78, 10, 'Python', 'sky', 54, 100, 60)
combined_tuples = tuple(set(tuple1) | set(tuple2))
dublicated_values = tuple(set(tuple1) & set(tuple2))

print(combined_tuples)
print(dublicated_values)


for i in tuple1:
    if i in tuple2:
       duplicated_values += (i,)
print(duplicated_values)



# number 4

tuple_numbers = (3, 6, 8, 9, 5)
changed_tuple = (tuple_numbers[-1],) + (tuple_numbers[1:-1]) + (tuple_numbers[0],)
print(changed_tuple)



# number 5

num_tuple = (2, 4, (14, 83, 22), 77, (15, (26, 57)))
full_tuple = ()
for i in num_tuple:
    if isinstance(i, tuple):
        for j in i:
            if isinstance(j, tuple):
                full_tuple += j
            else:
                full_tuple += (j,)
    else:
        full_tuple += (i,)
print(full_tuple)




# number 6

first_set = {2,5} 
second_set = {'n', 'i'}
new_set = {(i, j) for i in first_set for j in second_set}
print(new_set)


