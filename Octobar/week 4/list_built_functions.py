numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

numbers.sort()
print("Sorted list:", numbers)

min_value = min(numbers)
print("Minimum value:", min_value)

max_value = max(numbers)
print("Maximum value:", max_value)

count_num = len(numbers)
print("Length of list : ", count_num)

numbers.reverse()
print("Reversed list:", numbers)

total_sum = sum(numbers)
print("Sum of all elements:", total_sum)
