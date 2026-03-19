#personal bio card

#assigning variables
name="Harsha"
age=21
course="AI AND DS"
college="CMRIT"
email="harsha@gmail.com"

#make a fixed width for card
width=32

#displaying the bio card
print("|" + "="*width + "|")
print("|" + " BIO CARD".center(width) + "|")
print("|" + "="*width + "|")
#add .ljust(width+1) to match the top and bottom borders of the card
print(f"|Name   : {name}".ljust(width+1)+"|")
print(f"|Age    : {age}".ljust(width+1)+"|")
print(f"|Course : {course}".ljust(width+1)+"|")
print(f"|College: {college}".ljust(width+1)+"|")
print(f"|Email  : {email}".ljust(width+1)+"|")
print("|" + "="*width + "|")


