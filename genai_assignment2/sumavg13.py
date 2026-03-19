# Sum and Average Calculator

# Take input for count of numbers
count=int(input("How many numbers?"))

# Check if count is valid and then take numbers as input, calculate sum, average, max and min
if count<=0:
    print("Count must be a positive integer.")
else:
    numbers = []
    for i in range(1,count+1):
        num=float(input(f"Enter number {i}:"))
        numbers.append(num)

    total = sum(numbers)
    average = total / count
    max_num = max(numbers)
    min_num = min(numbers)

#display results
    print("\n==RESULTS==")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {max_num}")
    print(f"Minimum: {min_num}")