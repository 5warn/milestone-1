#WAP to find the index of an item in a tuple
my_tuple=(1,2,3,4,5)
item=int(input("Enter the item: "))
if item in my_tuple:
    index=my_tuple.index(item)
    print("Index of the item is:", index)
else:
    print("Item does not exist in the tuple")