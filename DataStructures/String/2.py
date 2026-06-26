#WAP to check whether palindrome or not
str1=input("Enter a string: ")
if str1==str1[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")