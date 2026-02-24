#factorial calculator

number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1.")
else:
    factorial = 1
    steps = " "

    for i in range(number,0,-1):
        factorial *= i
        steps +=str(i)
        if i!=1:
            steps +="x"
print(f"{number}! = {steps} = {factorial}")