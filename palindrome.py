num=int(input("enter a number"))
rev=0
n2=num
while num!=0:
    n1=num % 10
    rev=rev*10+n1
    num=num //10
if rev==n2:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")
    