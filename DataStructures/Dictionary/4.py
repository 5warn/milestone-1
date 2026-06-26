#WAP to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values
my_dict={1:10, 2:20, 3:30}

#printing only keys
print("Keys: ")
for key in my_dict:
    print(key)
    
#printing only values
print("Values: ")
for value in my_dict.values():
    print(value)

#printing both keys and values
for key, value in my_dict.items():
    print(key,':', value)