# Write a program to find the longest word in a txt file and print its length.
def find_longest_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
    return longest_word, len(longest_word)

file_to_analyze = 'IO_Operations/sample.txt'
longest_word, length = find_longest_word(file_to_analyze)
print(f"The longest word is '{longest_word}' with a length of {length}.")