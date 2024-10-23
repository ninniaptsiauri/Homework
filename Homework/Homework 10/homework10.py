# Zip 2 lists

lst1 = [10, 20, 30, 40, 50]
lst2 = ['Hi', 'White', 'World', 'Python', 'Go']
print(list(zip(lst1, lst2)))



# even numbers from list 

numbers1 = [10, 43, 78, 100, 13, 45, 66, 28, 37, 80]
even_numbers1 = list(filter(lambda x: x % 2 == 0, numbers1))
print(f"Even numbers: {even_numbers1}")




# lambda for positive numbers

params = [3, -4, 6, 0, 10, 56, -19, -2, 9]
positive_numbers = list(filter(lambda x: x > 0, params))
print(f"Positive numbers: {positive_numbers}")




# palindrome

txt_lst = ['Hello', 'level', 'time', 'Eve', 'Python', 'madam']
txt_lst = [word.lower() for word in txt_lst]
palindrome = list(filter(lambda word: word == word[::-1], txt_lst))
print(f"Palindrome: {palindrome}")




# multiply digits

from functools import reduce

def multiply():

    while True:
        try: 
            numbers = input("Please enter numbers separated with space: ")
            params = [int(num) for num in numbers.split()]
            result = reduce(lambda x, y: x * y, params)
            print("Product of numbers:", result)
            break           

        except ValueError:
            print("Invalid input, please enter only numbers.")

multiply()




# check string with ending

def check_ending():
    
    while True: 
        
        try: 
            lst = input("Please enter words separated with space: ").lower().split()
            end = input("Choose the ending to find matching words: ").lower()
            
            if not all(word.isalpha() for word in lst) or not  end.isalpha():
                raise TypeError
            
            matching_words = list(filter(lambda word: word.endswith(end), lst))
            
            if matching_words:
                print(f"Matching words: {matching_words}")
            else: 
                print("No matching words found")
            break
        
        except TypeError:
            print("Invalid input, you can use only letters.")

check_ending()


