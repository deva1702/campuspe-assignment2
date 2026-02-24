#ticket pricing system

age=int(input("Enter your age: "))
day=input("Enter the day of the week:").lower()
tickets=int(input("Enter the number of tickets: "))

if age<3:
    base_price=0
elif 3<=age<=12:
    base_price=150
elif 13<=age<=59:
    base_price=300
else:
    base_price=200

total_price=base_price*tickets

if day in ["friday","saturday", "sunday"]:
    discount=total_price*0.20
else:
    discount=0

final_price=total_price-discount

print("\n===TICKET PRICING DETAILS===")
print(f"Base Price per ticket: ₹{base_price}")
print(f"Number of Tickets: {tickets}")
print(f"Total Price before discount: ₹{total_price}")
print(f"Discount Applied: ₹{discount}")
print(f"Final Price: ₹{final_price}")