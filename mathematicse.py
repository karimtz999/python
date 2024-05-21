import cmath  # cmath module includes support for complex numbers

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the two solutions using quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return (root1, root2)

# Main program
if __name__ == "__main__":
    # Input coefficients
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    # Ensure a is not zero
    if a == 0:
        print("Coefficient a cannot be zero for a quadratic equation.")
    else:
        # Solve the equation
        roots = solve_quadratic(a, b, c)
        
        # Print the results
        print("The roots of the quadratic equation are:")
        print(f"Root 1: {roots[0]}")
        print(f"Root 2: {roots[1]}")
