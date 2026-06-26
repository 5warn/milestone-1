from sys import argv
l1=argv[1].split('-')
l2=argv[2].split('-')
l3=argv[3].split('-')
for i in l3:
    if i in l1:
        hap=+1
    if i in l2:
        hap=-1
print(hap)