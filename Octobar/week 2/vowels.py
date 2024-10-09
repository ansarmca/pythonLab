str="ansar"
vowels = ['a','e','i','o','u']
vowel_count=0

for char in str.lower():
    if char in vowels:
        vowel_count+=1
print("number of vowels in the string: ",vowel_count)
