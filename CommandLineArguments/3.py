from sys import argv
l1=argv[1:]
Sum=0
#check if no. is prime 
for i in l1:
    n=int(i)
    if n>1:
        for j in range(2,n):
            if (n%j)==0:
                break
        else:
            Sum+=n
print(Sum)
