list1 = list(map(int, input("Enter the first list of integers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of integers separated by spaces: ").split()))

if len(list1) == len(list2):
    print("a) The lists are of the same length.")
else:
    print("a) The lists are NOT of the same length.")

if sum(list1) == sum(list2):
    print("b) The lists sum to the same value.")
else:
    print("b) The lists do NOT sum to the same value.")

common_values = set(list1) & set(list2)
if len(common_values) > 0:
    print("c) Common values in both lists:", list(common_values))
else:
    print("c) No values occur in both lists.")
