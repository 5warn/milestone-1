#WAP to check if a given key already exists in a dictionary
my_dict={1:10, 2:20, 3:30}
key=int(input("Enter the key to check: "))
if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")