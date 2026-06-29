# Write a program to accept input from user and append it to a txt file.

def append_to_file(file_path, content):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content + '\n')

file_to_append = 'IO_Operations/sample.txt'
user_input = input("Enter text to append to the file: ")
append_to_file(file_to_append, user_input)