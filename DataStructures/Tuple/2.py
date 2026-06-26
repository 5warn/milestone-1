#WAP to check whether an element exists in a tuple or not
my_tuple=(1,2,3,4,5)
el=int(input("Enter the element to check: "))
if el in my_tuple:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")