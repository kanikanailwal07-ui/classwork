#input a sentence fro user
sentence = input("Enter a sentence: ")

#split the sentence into words
words = sentence.split()

#count the frequency of each word in the sentence
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

#display the frequency of each word
print("The frequency of each word in the sentence is:")
for word, frequency in word_frequency.items():
    print(word, ":", frequency)

#find the word with the highest frequency
most_frequent_word = max(word_frequency, key=word_frequency.get)
print("The word with the highest frequency is:", most_frequent_word, "with a frequency of", word_frequency[most_frequent_word])

#display all words in alphabetical order
print("The words in alphabetical order are:")

for word in sorted(word_frequency.keys()):
    print(word)

