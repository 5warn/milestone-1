# Write a program to accept the file name to be opened from the user, 
# if file exist print the contents of the file in title case or else handle the exception and print an error message.

def read_file_title_case():
    file_name = input("Enter the file name to open (e.g., sample.txt): ")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content.title())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist. Please check the name and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file_title_case()