# Grade Calculator

try:
    # List to store marks for each subject and variable to keep track of total marks
    subjects = []
    total_marks = 0

    # Taking marks for 5 subjects
    for i in range(1, 6):
        marks = float(input(f"Enter marks for subject {i} (out of 100): "))
        
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            exit()
        
        subjects.append(marks)
        total_marks += marks

    percentage = total_marks / 5

    # Grade Calculation
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    # Pass/Fail condition
    
    if all(mark >= 40 for mark in subjects):
        result = "Pass"  
    else :
        result = "Fail"

    #display results
    print("\n=== RESULT ===")
    print("Marks:", subjects)
    print("Total:", total_marks, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("Final Result:", result)

except ValueError:
    print("Invalid input! Please enter numeric values.")
