#WAP to find if a given no. is palindrome or not
num=int(input("Enter a number: "))
num2,rev=num,0
while num>0:
    rev=rev*10+num%10
    num=num//10
if rev==num2:
    print("The number is palindrome")
else:
    print("The number is not palindrome")