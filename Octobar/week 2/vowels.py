str="Ansar"
vowels = ['a','e','i','o','u','A','E','I','O','O']
vowel_count=0

for char in str:
    if char in vowels:
        vowel_count+=1
print("number of vowels in the string: ",vowel_count)