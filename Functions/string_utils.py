def is_palindrome(name):
    cleaned_name = name.replace(" ", "").lower()
    if cleaned_name == cleaned_name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."


def count_vowels(name):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in name if char in vowels)
    return f"No of vowels: {count}"

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char != " ":  
            freq[char] = freq.get(char, 0) + 1
            
    freq_str = ", ".join([f"{key} - {value}" for key, value in freq.items()])
    return f"Frequency of letters: {freq_str}"