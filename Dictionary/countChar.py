# We need an empty dictionary, to store and display the letter frequencies.
from operator import le


word_count = {}
word = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
count = 1
for i in range(len(text)):
    if(text[i] == " " or text[i] == "'" or text[i] == "." or text[i] == ","):
        continue
    if(text[i].lower() in word_count):
        word_count[text[i].lower()] += 1
    else:
        word_count[text[i].lower()] = count

# Iterate over every character in the string.
for char in text.casefold():
    # We're only counting letters and digits (no punctuation).
    if char.isalnum():
        word[char] = word.setdefault(char, 0) + 1  

print(word_count)
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)