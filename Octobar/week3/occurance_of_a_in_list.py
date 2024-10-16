first_names = ["Alice", "Anas", "Raheem", "fazil"]

a_count = 0

for name in first_names:
    a_count += name.lower().count('a')

print("The letter 'a' occurs", a_count, "times in the list.")
