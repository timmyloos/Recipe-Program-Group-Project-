#!/usr/bin/env python3
# Midterm Exam - Answer the following three questions within 40 minutes





# 1. Create a loop to ask the user for input. The input should be an integer.

# Take the number from the input and add any integers that came before it, all the way to 0

# Ex. If you choose 5 as input, the loop should add 5, 4, 3, 2, 1, and 0 together.

# 5 points



# Enter your code here:

num = int(input("Enter an integer: "))

sum = 0

for x in range(num + 1):
	sum += x
	
print(sum)



# 2. Create a program that allows you to add items to a list and recall its contents

# The recall of the list should print the items individually, without any

# additional marks (hint: do not just print the list)

#15 points


# Enter your code here:

list= []

while True:
	item = input("Enter an item (press enter to stop adding): ")
	if not item:
		break
	list.append(item)
	
print("Items in the list:")
for item in list:
	print(item)
	





# 3. Create a menu using if, elif, else statements.

# The menu should have four options:

# Option 1 should add two numbers, inputs from the user

# Option 2 should get the square of one number, user input

# Option 3 should give a famous quote at random (3+ quotes)

# Option 4 should exit the program

# Anything else is up to you.

#20 points



# Enter your code here:

import random

while True:
		print("Menu:")
		print("1. Add two numbers")
		print("2. Square a number")
		print("3. Random famous quote")
		print("4. Exit program")
	
		choice = input("Enter your choice: ")
	
		if choice == "1":
				num1 = float(input("Enter first number: "))
				num2 = float(input("Enter second number: "))
				result = num1 + num2
				print("The sum is:", result)
			
		elif choice == "2":
				num = float(input("Enter a number: "))
				result = num ** 2
				print("The square is:", result)
			
		elif choice == "3":
				quotes = ["Be the change you wish to see in the world. - Mahatma Gandhi", 
									"I have a dream. - Martin Luther King Jr.",
					"I have no special talent. I am only passionately curious. - Albert Einstein"]
			
				quote = random.choice(quotes)
				print("Random Quote:", quote)
			
		elif choice == "4":
				print("Exiting program...")
				break
	
		else:
				print("Please pick a number between 1-4.")
			




	