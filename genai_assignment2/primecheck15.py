#Prime Number Checker

#define a function to check if a number is prime
def is_prime(num):
    if num<=1:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True

#take user input for a number and check if it's prime
number=int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#check for prime numbers in a given range
start=int(input("Enter start of range: "))
end=int(input("Enter end of range: "))
print(f"Prime numbers between {start} and {end}:")
for num in range(start,end+1):
    if is_prime(num):
        print(num,end=" ")
    

