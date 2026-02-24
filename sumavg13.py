# Sum and Average Calculator

count=int(input("How many numbers?"))

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

    print("\n==RESULTS==")
    print(f"Sum:",total)
    print(f"Average: {average}")
    print(f"Maximum: {max_num}")
    print(f"Minimum: {min_num}")