# anagrams

def check_anagrams(str1: str, str2: str):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)

string1 = input("Please enter a text: ")
string2 = input("Please enter a text: ")

if check_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")




# character in string

def character_in_txt(string: str, char: str):
    return string.count(char)

string = input("Please enter a text: ")
char = input("Please enter a character: ")
result = character_in_txt(string, char)
print(f"The character '{char}' appears {result} times in the text.")




# Fibonacci 

def fibonacci(n: int):
    fib_sequene = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequene.append(a)
        a, b = b, a + b
    return fib_sequene

while True:
    num = int(input("Please enter a positive number: "))
    if num <= 0:
        continue
    else:
        result = fibonacci(num)
        print(result)
        break

