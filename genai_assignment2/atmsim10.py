#Simple ATM Simulator

balance=10000

transaction_history = []  # List to store transactions

#Stores transaction details
def add_transaction(transaction_type, amount):
    transaction_history.append(f"{transaction_type} | Amount: ₹{amount} | Balance: ₹{balance}")

while True:
    print("\n=== ATM SIMULATOR ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transaction History")
    print("5. Exit")

    choice=input("Enter you choice:")

#check balance, deposit, withdraw, exit
    if choice=="1":
        print(f"your current balance is: ₹{balance}")

    elif choice=="2":
        amount=float(input("enter the amount to deposit:"))
        if amount<=0:
            print("Invalid amount! Please enter a positive number.")
        else:
            balance+=amount
            print(f"₹{amount} deposited successfully. New balance: ₹{balance}")
            add_transaction("Deposit", amount)

    elif choice=="3":
        amount=float(input("enter the amount to withdraw:"))
        if amount<=0:
            print("Invalid amount! Please enter a positive number.")
        elif balance-amount<500:
            print("Minimum balance ₹500 must remain.")
        else:
            balance-=amount
            print(f"₹{amount} withdrawn successfully. New balance: ₹{balance}")
            add_transaction("Withdrawal", amount)   
    
    elif choice=="4":
        if not transaction_history:
            print("No transactions yet.")
        else:
            print("\n=== TRANSACTION HISTORY ===")
            for transaction in transaction_history:
                print(transaction)

    elif choice=="5":
        print("Thank you for using the ATM Simulator. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")