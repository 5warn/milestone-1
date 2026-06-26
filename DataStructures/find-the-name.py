#help Alex find out how many times is name is in a string of n length
string=input("Enter a string: ")
if len(string)>0 and len(string)<=200:
    count=string.count("alex")
    print(count)