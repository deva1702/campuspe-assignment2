#Text Analysis Functions

#function to count words in a text
def count_words(text):
    words = text.split()
    return len(words)

#function to count vowels in a text
def count_vowels(text):
    return sum(1 for char in text if char.lower() in 'aeiou')

#function to count consonants in a text
def count_consonants(text):
    return sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou')

#function to reverse the text
def reverse_text(text):
    return text[::-1]

#function to check if the text is a palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ","")
    return cleaned == cleaned[::-1]

#function to remove vowels from the text
def remove_vowels(text):
    return ''.join(char for char in text if char.lower() not in 'aeiou')

#function to count word frequencies in the text
def word_frequencies(text):
    words = text.split()
    frequencies = {}
    for word in words:
        word = word.lower()
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

#function to find the longest word in the text  
def longest_word(text):
    words= text.split()
    if not words:
        return None
    longest = max(words, key=len)
    return longest

#main function to analyze the text and display results
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))
    print("Word Frequency:", word_frequencies(text))

    longest = longest_word(text)
    print("Longest word:", longest, f"({len(longest)} letters)")

user_text = input("Enter text: ")
analyze_text(user_text)