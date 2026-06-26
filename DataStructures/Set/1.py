#WAP to remove a given item from set
my_set={1,2,3,4,5}
item=int(input("Enter the item to remove: "))
if item in my_set:
    my_set.remove(item)
    print(my_set)
else:
    print("Item does not exist in the set")