start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

even_digits_squares = []
for num in range(start, end + 1):
    
    even_digits = True
    for digit in str(num):
        if int(digit) % 2 != 0:
            even_digits = False
            break

    if even_digits and int(num ** 0.5) ** 2 == num:
        even_digits_squares.append(num)

print("List of 4-digit numbers with all even digits and perfect squares:")
print(even_digits_squares)
