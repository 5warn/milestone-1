import re
from collections import Counter

def find_secret_message(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    num_lines = len(lines)
    if num_lines < 1:
        print("The file has no valid lines.")
        return
    
    if num_lines == 12:
        meeting_time = "12 PM"
    elif num_lines == 24:
        meeting_time = "12 AM"
    else:
        meeting_time = f"{num_lines} AM"

    all_words = []
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())
        all_words.extend(words)

    if not all_words:
        print("No valid words found in the file.")
        return
    word_counts = Counter(all_words)
    most_common_word, _ = word_counts.most_common(1)[0]
    meeting_place = f"{most_common_word.capitalize()} Street"
    print(f"Meeting time: {meeting_time}")
    print(f"Meeting place: {meeting_place}")

file_to_read1 = 'IO_Operations/mini project/sample1.txt'  
find_secret_message(file_to_read1)
file_to_read2 = 'IO_Operations/mini project/sample2.txt'  
find_secret_message(file_to_read2)