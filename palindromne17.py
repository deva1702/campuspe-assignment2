#palindrome checker

user_input = input("enter the input:")

original=user_input
cleaned=user_input.lower()
reversed_text=cleaned[::-1]

print("original:",original)
print("cleaned:",cleaned)
print("reversed:",reversed_text)
if cleaned==reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")