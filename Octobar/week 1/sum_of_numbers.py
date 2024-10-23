my_list = []

n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    value = int(input("Enter a number: "))
    my_list.append(value)

total = 0

for item in my_list:
    total += item

print("The sum of the list is:", total)
