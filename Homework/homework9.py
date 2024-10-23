# add item into global list

int_list = [10,20,30,40]

def add_item(num):
    global int_list
    int_list.append(num)

number = int(input("Please enter a number: "))
add_item(number)
print(int_list)




# sum of digits

def sum_of_digits(number):
    
    if number == 0:
        return 0
    else:
        return (number % 10) + sum_of_digits(number // 10)

num1 = int(input("Please enter a number: "))
result = sum_of_digits(num1)
print(f"Sum of digits in {num1} is: {result}")




# reversed string

def reverse_str(txt):
    if txt == "":
        return txt
    else:
        return txt[-1] + reverse_str(txt[:-1])


str = input("Please enter a text: ")
result = reverse_str(str)
print(f"Reversed text: {result}")





# fibonacci sequence

def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Please enter a number to get Fibonacci sequnce: "))
if n > 0:
    print([fibonacci(i) for i in range(n)])
else:
    print([0])
