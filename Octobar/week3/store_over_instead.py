user_input = input("Enter a list of integers separated by spaces: ")
input_list = list(map(int, user_input.split()))

output_list = []
for x in input_list:
    if x > 100:
        output_list.append("over")
    else:
        output_list.append(x)

print("Modified list:")
for item in output_list:
    print(item)
