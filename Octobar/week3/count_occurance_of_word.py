# Input line of text
text = input("Enter a line of text: ")

# Split the text into words
words = text.split()

# Create a dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print("'" + word + "' occurs " + str(count) + " times.")
