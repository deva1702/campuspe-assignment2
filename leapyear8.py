# Leap Year Checker

try:
    year = int(input("Enter a year: "))

    #leap year rules:
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(f"{year}")
        print(f"{year}: a LEAP year.")
        print("Reason: Divisible by 4 and satisfies century rule.")
    else:
        print(f"{year}")
        print(f"{year} : NOT a leap year.")
        print("Reason: Does not satisfy leap year conditions.")

except ValueError:
    print("Invalid year entered.")
