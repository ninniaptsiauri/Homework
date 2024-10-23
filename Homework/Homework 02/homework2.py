# even or odd
number = int(input("Please enter a number: "))
if(number % 2) == 0:
    print("Even")
else:
    print("Odd")


# check words in a list
list = ["small", "tall", "middle"]
word1 = "small"
word2 = "tall"
word3 = "middle"
text = input("Please enter your text: ")
if word1 in text:
    print(word1)
if word2 in text:
     print(word2)
if word3 in text:
     print(word3)
if word1 not in text and word2 not in text and word3 not in text:
    print("We haven't found words from the list in your text")


# calculator 
number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number: "))
operator = input("Please choose an operation: ")
if operator == '+' :
    add = number1 + number2
    print("Addition:", add)
elif operator == '-' :
    subs = number1 - number2
    print("Substraction is:", subs)
elif operator == '*' :
    mult = number1 * number2
    print("Multiplication:", mult)
elif operator == '/' :
    div = number1 / number2
    print("Division:", div)
elif operator == '//' :
    fl = number1 // number2
    print("Floor division:", fl)
elif operator == '%' :
    mod = number1 % number2
    print("Modulus:", mod)
elif operator == '**' :
    exp = number1 ** number2
    print("Exponentiation:", exp)
else:
    print("Sorry, you entered invalid operator.")

