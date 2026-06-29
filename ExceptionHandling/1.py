# Write a program to accept two numbers from the user and perform division. 
# If any exception occurs, print an error message or else print the result.
def perform_division():
    try:
        num1 = float(input("Enter the first number (numerator): "))
        num2 = float(input("Enter the second number (denominator): "))
        result = num1 / num2
        
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The result of the division is: {result}")

perform_division()