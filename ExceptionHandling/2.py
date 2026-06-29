# Write a program to accept a number from the user and check whether it’s prime or not. 
# If user enters anything other than number, handle the exception and print an error message.

def check_prime_with_handling():
    try:
        number = int(input("Enter an integer to check if it's prime: "))
        if number <= 1:
            print(f"{number} is not a prime number.")
            return          
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break                
        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")            
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

check_prime_with_handling()