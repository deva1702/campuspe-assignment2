#age calculator

from datetime import datetime

#ask the user for their birth date
birth_date_str = input("Enter your birth date (DD/MM/YYYY): ")
birth_date=datetime.strptime(birth_date_str, "%d/%m/%Y")

today = datetime.today()

#calculate age
age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
age_months = age_years * 12 + today.month - birth_date.month 
age_days = (today - birth_date).days
age_hours = age_days * 24
age_minutes = age_hours * 60
age_until_100 = 100 - age_years

#display the age
print(f"Date of Birth: {birth_date_str}")
print(f"Current Age: {age_years} years")
print(f"Current Age in years: {age_years} years")
print(f"current age in months: {age_months} months")
print(f"current age in days: {age_days} days")  
print(f"current age in hours: {age_hours} hours")
print(f"current age in minutes: {age_minutes} minutes")
print(f"You will turn 100 years old in {age_until_100} years.")
