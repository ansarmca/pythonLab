# Create an empty list
user_list = []

# Get the number of elements from the user
num_elements = int(input("How many elements do you want to add? "))

# Use a loop to input each element
for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)

# Print the final list
print("The list is:", user_list)
