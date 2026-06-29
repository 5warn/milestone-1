def sort_colors(color_string):
    color_list = color_string.split('-')
    color_list.sort()
    return '-'.join(color_list)

# Sample 1
input_1 = "green-red-yellow-black-white"
print("Output 1:", sort_colors(input_1))

# Sample 2
input_2 = "PINK-BLUE-TAN-PURPLE"
print("Output 2:", sort_colors(input_2))
