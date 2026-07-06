#input of sentence
sentence = input("Enter a sentence: ")
#initialize vowel count as 
vowel = 0
for x in sentence:
   if (x == 'a' or x =='A' or x == 'e' or x == 'E' or x == 'i' or x == 'I' or x == 'o' or x == 'O' or x == 'u' or x == 'U'):
#increment vowel count
       vowel += 1

#---------------------------------------------------

print("number of vowels=", vowel)