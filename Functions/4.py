#Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count_letters(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")

sample_input = "Hello World!"
count_letters(sample_input)