# Declare a list with 10 integers and ask the user to enter an index. 
# Check whether the number in that index is positive or negative number. 
# If any invalid index is entered, handle the exception and print an error message.

def check_index_sign():
    numbers_list = [12, -5, 0, 45, -23, 89, -1, 7, -14, 50]
    try:
        index = int(input("Enter an index (0 to 9) to check the number: "))
        value = numbers_list[index]
        if value > 0:
            print(f"The number at index {index} is {value}, which is Positive.")
        elif value < 0:
            print(f"The number at index {index} is {value}, which is Negative.")
        else:
            print(f"The number at index {index} is {value}, which is Zero.")
    except IndexError:
        print("Error: Invalid index! Please enter an index between 0 and 9.")  
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer index.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 
    
check_index_sign()