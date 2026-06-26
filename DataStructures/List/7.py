#WAP to remove the item from a specified position in a list
my_list=[1,2,3,4,5]
pos=int(input("Enter the position of the item to remove: "))
if pos>=0 and pos<len(my_list):
    my_list.pop(pos)
    print(my_list)