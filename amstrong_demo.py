num=int(input("enter number : "))
s=0
n2=num
while num!=0:
    n1=num % 10
    s=s+(n1^(3))
    num=num //10
if n2==s:
    print("given number is amstrong")
else:
    print("given number is not amstrong")