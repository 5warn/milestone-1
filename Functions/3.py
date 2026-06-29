# Write a function to calculate and return the factorial of a number (a non-negative integer).

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

sample_input = 5
result = calculate_factorial(sample_input)
print(result)
