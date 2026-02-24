# Temperature Converter

while True:
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Exit program.")
        break

    try:
        if choice == "1":
            temp = float(input("Enter the temperature in Celsius: "))
            print(f"Temperature: {temp:.2f} °C")
            result = (temp * 9/5) + 32
            unit="°F"
        elif choice == "2":
            temp = float(input("Enter the temperature in Fahrenheit: "))
            print(f"Temperature: {temp:.2f} °F")
            result = (temp - 32) * 5/9
            unit="°C"
        elif choice == "3":
            temp = float(input("Enter the temperature in Celsius: "))
            print(f"Temperature: {temp:.2f} °C")
            result = temp + 273.15
            unit="K"
        elif choice == "4":
            temp = float(input("Enter the temperature in Kelvin: "))
            print(f"Temperature: {temp:.2f} K")
            result = temp - 273.15
            unit="°C"
        elif choice == "5":
            temp = float(input("Enter the temperature in Fahrenheit: "))
            print(f"Temperature: {temp:.2f} °F")
            result = (temp - 32) * 5/9 + 273.15
            unit="K"
        elif choice == "6":
            temp = float(input("Enter the temperature in Kelvin: "))
            print(f"Temperature: {temp:.2f} K")
            result = (temp - 273.15) * 9/5 + 32
            unit="°F"
        else:
            print("Invalid choice!")
            continue

        
        print("Converted Temperature:", round(result, 2), unit)

    except ValueError:
        print("Invalid temperature entered.")
