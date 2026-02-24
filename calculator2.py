#simple calculator
try:
	#ask the user for two numbers
	num1 = float(input("enter the first number:"))
	num2 = float(input("enter the second number:"))

	print("Results:")
	print(f"{num1} + {num2} = {num1 + num2}")
	print(f"{num1} - {num2} = {num1 - num2}")
	print(f"{num1} * {num2} = {num1 * num2}")
	print(f"{num1} / {num2} = {num1 / num2:.2f}" if num2 != 0 else "Cannot divide by zero")
	print(f"{num1} % {num2} = {num1 % num2 if num2 != 0 else 'Cannot compute modulo with zero'}")
	print(f"{num1} ** {num2} = {num1 ** num2}")
	
except ValueError:
	#handle input that cannot be converted to float
	print("Error: Please enter valid numbers")