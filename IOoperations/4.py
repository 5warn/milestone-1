# Write a program to read a txt file line-by-line and store it into a list.
def read_file_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]
    
file_to_read = 'IO_Operations/sample.txt'
lines_list = read_file_to_list(file_to_read)
print(lines_list)