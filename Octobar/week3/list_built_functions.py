# Input a list of numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Find the minimum value
min_value = min(numbers)
print("Minimum value:", min_value)

# Find the maximum value
max_value = max(numbers)
print("Maximum value:", max_value)

# Count the occurrences of a specific number (e.g., 45)
num_to_count = int(input("Enter the number to count: "))
count_num = numbers.count(num_to_count)
print("Occurrences of", num_to_count, ":", count_num)

# Sort the list in ascending order
numbers.sort()
print("Sorted list:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

# Calculate the sum of all elements
total_sum = sum(numbers)
print("Sum of all elements:", total_sum)
