# Input a list of first names
first_names = ["Alice", "Anna", "Jack", "Amanda", "Sarah"]

# Initialize a counter for occurrences of 'a'
a_count = 0

# Iterate through each name and count 'a'
for name in first_names:
    a_count += name.lower().count('a')  # Use lower() to count both 'a' and 'A'

# Print the total count of 'a'
print("The letter 'a' occurs", a_count, "times in the list.")
