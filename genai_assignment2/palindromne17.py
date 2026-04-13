#palindrome checker

#take user input
user_input = input("enter the input:")

#clean the input by converting to lowercase and removing spaces and reverse the cleaned input
original=user_input
cleaned=user_input.lower()
reversed_text=cleaned[::-1]

#display original input, cleaned input and reversed input
print("original:",original)
print("cleaned:",cleaned)
print("reversed:",reversed_text)

#check if cleaned input is the same as reversed input to determine if it's a palindrome
if cleaned==reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")