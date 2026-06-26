#WAP to replace last value of tuples in a list to 100
my_list=[(10,20,40),(48,50,60),(70,80,90)]
new_list=[]
for t in my_list:
    new_tuple=t[:-1]+(100,)
    new_list.append(new_tuple)
print("List after replacing last value of tuples:", new_list)