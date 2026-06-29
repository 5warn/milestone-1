# Write a program to read the entire content from a txt file and display it to the user.

def read_and_display_file(file_path, display=True):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if display:
            print(content)
        return content


file_to_read = 'IO_Operations/sample.txt'  
read_and_display_file(file_to_read)