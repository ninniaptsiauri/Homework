# check if user's input text is a palindrome

txt = input("Please enter a text: ")
if txt == txt[::-1]:
    print("Your entered text is a palindrome")
else:
    print("Your entered text isn't a palindrome")




# convert user's input into ASCII standard

txt = input("Please enter a text: ")
print("This text in ASCII standard is:")
for i in txt:
    print(ord(i))

    