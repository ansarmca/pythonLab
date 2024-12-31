from math_operations.factorial import factorial
from math_operations.fibonacci import fibonacci
from math_operations.summation.sum_numbers import sum_of_n_numbers

def main():
    print("Choose an operation:")
    print("1. Factorial")
    print("2. Fibonacci")
    print("3. Sum of n numbers")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        n = int(input("Enter a number for factorial: "))
        print(f"Factorial of {n} is {factorial(n)}")
    elif choice == 2:
        n = int(input("Enter the number of terms for Fibonacci sequence: "))
        print(f"Fibonacci sequence with {n} terms: {fibonacci(n)}")
    elif choice == 3:
        n = int(input("Enter a number for sum calculation: "))
        print(f"Sum of first {n} numbers is {sum_of_n_numbers(n)}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
