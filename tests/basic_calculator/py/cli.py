import sys

def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers and log the operation details.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Sum of the two numbers
    """
    print(f"Starting addition operation with inputs: {a} and {b}")
    
    try:
        result = a + b
        print(f"Successfully calculated sum: {result}")
        return result
    except Exception as e:
        print(f"Error during addition: {str(e)}")
        raise

# Check if correct number of arguments are provided
if len(sys.argv) != 3:
    print("Exactly 2 numbers are required as arguments")
    print("Usage: python script.py <number1> <number2>")
    sys.exit(1)

try:
    # Convert command line arguments to float
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    
    # Calculate and print result
    result = add_numbers(num1, num2)
    print(f"Sum: {result}")
    
except ValueError:
    print("Invalid input: Please provide valid numbers")
    print("Error: Please provide valid numbers")
    sys.exit(1)