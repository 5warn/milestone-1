#WAP to remove the first occurance of a specified element from a list
my_list=[1,2,3,4,4,3,3,5]
el=int(input("Enter the element to remove: "))
if el in my_list:
    my_list.remove(el)
    print(my_list)