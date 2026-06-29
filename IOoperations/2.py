# Write a program to read first n lines from a txt file. Get n as user input.
def read_first_n_lines(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [next(file) for _ in range(n)]
        return lines


file_to_read = 'IO_Operations/sample.txt'
n = int(input("Enter the number of lines to read: "))
first_n_lines = read_first_n_lines(file_to_read, n)
for line in first_n_lines:
    print(line, end='')