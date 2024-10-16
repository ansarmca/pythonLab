user_list = []

num_elements = int(input("How many elements do you want to add? "))

for i in range(num_elements):
    element = input("Enter element :" )
    user_list.append(element)

print("The list is:", user_list)
