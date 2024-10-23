#countdown from user's input 
num = int(input("Please enter a number: "))
while num > 0:
   print(num)
   num -= 1


#ask user to input number until type 'sum'
total_sum = 0
while True:
    num = input("Please enter a number, or type 'sum' to finish: ")
    if num.lower() == 'sum':
        print("Total of your entered positive numbers is:", total_sum)
        break
    num = int(num)
    if num > 0:
        total_sum += num


#program chooses random number and ask user to guess this number
import random
number = random.randint(1, 100)
tries = 10 
while tries > 0:
    guess = int(input("Please choose a number from 1 to 100: "))
    tries -= 1
    if guess == number:
      print("You guessed the number:", number)
      break
    elif guess > number:
      print("Your number is greater")
    elif guess < number:
      print("Your number is less")
else:
   print("Sorry, you used all your chances.")
