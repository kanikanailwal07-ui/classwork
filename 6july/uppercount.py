#input of sentence
sentence = input("Enter a sentence: ")
#initialize upper case count and lower case count as 
upper_count = 0
lower_count = 0
for char in sentence:
   if (char >= 'A' and char <= 'Z'):
      upper_count += 1
   elif (char >= 'a' and char <= 'z'):
      lower_count += 1
#---------------------------------------------------
print("number of upper_count=", upper_count)
print("number of lower_count=", lower_count)