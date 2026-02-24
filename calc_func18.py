#Calculator Functions

import math
# Function to perform addition
def add(a,b):
    return a+b

# Function to perform subtraction
def subtract(a,b):
    return a-b

# Function to perform multiplication
def multiply(a,b):  
    return a*b

# Function to perform division
def divide(a,b):
    if b==0:
        return "division by zero is not allowed"
    else:
        return a/b
    
# Function to perform modulus
def modulus(a,b):
    if b==0:
        return "modulus by zero is not allowed"
    else:
        return a%b
    
# Function to perform power
def power(a,b):
    return a**b

#function to perform square root
def square_root(a):
    if a<0:
        return "square root of negative number is not defined"
    else:
        return math.sqrt(a)
    
def percentage(a,b):
    if b==0:
        return "percentage with zero as total is not defined"
    else:
        return (a/b)*100
    
def calculator():
    while True:
        print("\n=== CALCULATOR FUNCTIONS ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "9":
            print("Exiting calculator.")
            break
        try:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))  
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == "1":
            print("Result:", add(a,b))
        elif choice == "2":
            print("Result:", subtract(a,b))
        elif choice == "3":
            print("Result:", multiply(a,b))
        elif choice == "4":
            print("Result:", divide(a,b))
        elif choice == "5":
            print("Result:", modulus(a,b))
        elif choice == "6":
            print("Result:", power(a,b))
        elif choice == "7":
            print("Result:", square_root(a))
        elif choice == "8":
            print("Result:", percentage(a,b)) 
        else:
            print("Invalid choice! Please select a number between 1 and 9.")

calculator()
            