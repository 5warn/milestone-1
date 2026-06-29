#Write a function to print the even numbers from a given list. List is passed to the function as an argument.

def print_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    print("Even numbers:", even_numbers)

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(sample_list)