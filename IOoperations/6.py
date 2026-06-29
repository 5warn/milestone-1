# Write a program to count the frequency of words in a txt file.
def count_word_frequency(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
        frequency = {}
        for word in words:
            word = word.lower()  # Convert to lowercase for case-insensitive counting
            frequency[word] = frequency.get(word, 0) + 1
    return frequency

file_to_analyze = 'IO_Operations/sample.txt'
word_frequency = count_word_frequency(file_to_analyze)
for word, freq in word_frequency.items():
    print(f"'{word}': {freq}")