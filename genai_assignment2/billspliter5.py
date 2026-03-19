#Bill Spliter

try:
    #take user input for total bill, number of people, tax percentage and tip percentage
    total_bill = float(input("Enter the total bill amount: "))
    num_people = int(input("Enter the number of people splitting the bill: "))
    tax_percentage = float(input("Enter the tax percentage in %: "))
    tip_percentage = float(input("Enter the tip percentage in %: "))

    #calculate tax amount, tip amount, total bill and amount per person
    tax_amount = total_bill * (tax_percentage / 100)
    after_tax= total_bill + tax_amount
    tip_amount = after_tax * (tip_percentage / 100)
    total= after_tax + tip_amount
    amount_per_person = total / num_people

    #display results
    print("\n===BILL SPLITER RESULTS===")
    print(f"subtotal: ${total_bill:.2f}")
    print(f"tax amount: ${tax_amount:.2f}")
    print(f"amount after tax: ${after_tax:.2f}")
    print(f"tip amount: ${tip_amount:.2f}")
    print(f"total bill: ${total:.2f}")
    print(f"amount per person: ${amount_per_person:.2f}")

except ValueError:
    print("Error: Please enter valid numbers.")