#Number Pattern Printer

#display pattern options
print("\n choose pattern:")
print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")
print("5. Pattern 5")
print("6. Pattern 6")
print("7. Pattern 7")

#take user input for pattern choice and height
choice=int(input("Enter your choice: "))
height=int(input("Enter the height of the pattern: "))

#validate height and display pattern based on user choice
if height<=0:
    print("Height must be a positive integer.")
else:
    print("\n Pattern Output")

#perform pattern printing based on user choice
    if choice==1:
        for i in range(1,height+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()
    
    elif choice==2:
        for i in range(1,height+1):
            for j in range(i):
                print(i,end=" ")
            print()
    
    elif choice==3:
        for i in range(height,0,-1):
            for j in range(i,0,-1):
                print(j,end=" ")
            print()

    elif choice==4:
        for i in range(1,height+1):
            print(" "*(height-i),end="")
            for j in range(1,i+1):
                print(j,end="")
            for j in range(i-1,0,-1):
                print(j,end="")
            print()

    elif choice==5:
        for i in range(1,height+1):
            print(" "*(height-i),end="")
            for j in range(1,i+1):
                print(i,end=" ")
            print()

    elif choice==6:
        for i in range(1,height+1):
            print(" "*(height-i),end="")
            for j in range(1,i+1):
                print(j,end=" ")
            print()

    elif choice==7:
        for i in range(1,height+1):
            print(" "*(height-i),end="")
            for j in range(i,0,-1):
                print(j,end=" ")
            print()
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
