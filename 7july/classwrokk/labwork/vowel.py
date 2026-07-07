# Define a function to count vowels in a given text
def count_vowels(text):
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Define a set of vowels for easy checking
    vowels = set("aeiouAEIOU")
    
    # Iterate through each character in the text
    for char in text:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

# Main program to accept a sentence from the user and display the total number of vowels
sentence = input("Enter a sentence:\n")
total_vowels = count_vowels(sentence)
print(f"\nTotal Vowels: {total_vowels}")