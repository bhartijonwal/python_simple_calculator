#Python program to make a simple calculator

# 3 steps to build calculator program:
   # 1. functions for operations
   # 2. user input
   # 3. print result

#  Step 1 - Create functions for operations

# Functions to add two numbers
def add(a,b):
    return a + b 

# Functions to subtract two numbers
def subtract(a,b):
    return a - b 

# Functions to multiply two numbers
def multiply(a,b):
    return a * b

# Functions to divide two numbers
def divide(a,b):
    return a / b

# Functions to find the average of two numbers
def avg(a, b):
    return (a+ b)/2 
 
# Step 2 - Take user input

print("Please select the operation you want to perform:\n" \
      "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n" \
        "5. Average\n")

select = int(input("Enter your choice of operation from 1, 2, 3, 4, 5: "))
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:")) 

# Step 3 - Print result
if select == 1:
    print(num1, "+", num2, "=", add(num1,num2))
elif select == 2:
    print(num1, "-", num2, "=", subtract(num1,num2))
elif select == 3:
    print(num1, "*", num2, "=", multiply(num1,num2))
elif select == 4:
    print(num1, "/", num2, "=", divide(num1,num2))
elif select == 5:
    print("The average of", num1, "and", num2, "is", avg(num1,num2))
else:
    print("Invalid input! Please select a valid operation from 1, 2, 3, 4, 5.")
    