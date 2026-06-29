f1=open("ExceptionHandling/purchase-1.txt","r")
item_pur=0
item_free=0
total=0
dis=0
while f1.readline()!= "":
    try:
        line=f1.readline()
        item,price=line.split(" ")
        item_pur+=1
        total+=int(price)

    except ValueError:
        print("Error: Invalid line format")
    print('1',f1.readline())
        
while f1.readline()!= "":
    try:
        line=f1.readline()
        l2=line.split(" ")
        item_free+=1
    
    except ValueError:
        print("Error: Invalid line format")
    print('2',f1.readline())    
while f1.readline()!= "":
    try:
        line=f1.readline()
        dis=line.split(" ")[1]
        
    except ValueError:
        print("Error: Invalid line format")
    print('3',f1.readline())   
print('Enter the file name:' + 'Purchase-1')
print('No of items purchased:',item_pur)
print('No of free items:',item_free)
print('Amount to pay:',total)
print('Discount given:',dis)
print('Final amount paid:',total-int(dis))

