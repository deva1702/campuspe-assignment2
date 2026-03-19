# Multiplication Table Generator

#take user input for number and range
number = int(input("Enter number: "))
end_range = int(input("Enter range (end): "))

#calculate and display multiplication table
if end_range <= 0:
    print("Range must be positive.")
else:
    print(f"\nMultiplication Table of {number}")
    for i in range(1, end_range + 1):
        print(f"{number} x {i} = {number * i}")

#display full multiplication table from 1 to 10
print("full multi[plication table (1 to 10):")
for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:4}", end=" ")
    print()

