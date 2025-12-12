# Simple Calculator
# A basic calculator that performs addition, subtraction, multiplication, and division

def add(a, b):
    """
    Adds two numbers together.
    
    Parameters:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first number.
    
    Parameters:
        a: First number (minuend)
        b: Second number (subtrahend)
    
    Returns:
        The difference (a - b)
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers together.
    
    Parameters:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second number.
    
    Parameters:
        a: First number (dividend)
        b: Second number (divisor)
    
    Returns:
        The quotient (a / b)
    
    Note:
        Returns an error message if trying to divide by zero
    """
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    """
    Main calculator function that provides a simple menu interface.
    Allows users to perform basic arithmetic operations.
    """
    print("\n=== Simple Calculator ===")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Result: {num1} × {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Result: {num1} ÷ {num2} = {result}")
            except ValueError:
                print("Error: Please enter valid numbers!")
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    calculator()