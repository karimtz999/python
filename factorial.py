def factorial(n):
    """
    Recursively computes the factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main program
if __name__ == "__main__":
    # Input from the user
    number = int(input("Enter a non-negative integer: "))
    
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Compute factorial
        result = factorial(number)
        
        # Print the result
        print(f"The factorial of {number} is: {result}")
