import string_utils

def test_string_functions(input_name):
    print(f"Sample input: {input_name}")
    print(string_utils.is_palindrome(input_name))
    print(string_utils.count_vowels(input_name))
    print(string_utils.frequency_of_letters(input_name))

# Test case 1
test_string_functions("bob")

# Test case 2
test_string_functions("marcel bentok tanaka")