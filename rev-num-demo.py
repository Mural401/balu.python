num=int(input("enter a number"))
rev=0
while num!=0:
    n1=num % 10
    rev=rev*10+n1
    num=num //10

print("reverse number : ",rev)
