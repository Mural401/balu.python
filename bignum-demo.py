a=int(input("enter a value : "))
b=int(input("enter b value : "))
c=int(input("enter c value : "))
d=int(input("enter d value : "))
if a>b and a>c and a>d:
    print("A is big value")
elif b>a and b>c and b>d:
    print("B is big value")
elif c>a and c>b and c>d:
    print("C is big value")
else:
    print("D is big value")
