#factorial calculator

#take user input for a number
number = int(input("Enter a number: "))
if number < 0: #factorial is not defined for negative numbers
    print("Factorial is not defined for negative numbers.")
elif number == 0: #factorial of 0 is 1
    print("Factorial of 0 is 1.")
else:
    factorial = 1 #initialize factorial variable
    steps = " "

    #calculate factorial and build the steps string
    for i in range(number,0,-1):
        factorial *= i
        steps +=str(i)
        if i!=1:
            steps +="x"
print(f"{number}! = {steps} = {factorial}")