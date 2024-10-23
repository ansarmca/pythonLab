words = input("Enter a sentence: ").split()

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
print("Length of longest word:", len(longest_word))
