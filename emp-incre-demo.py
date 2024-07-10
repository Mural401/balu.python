eid=int(input ("enter eid : "))
ename=input("enter ename : ")
esal=int(input("enter sal : "))
deptno=int(input("enter a deptno : "))
comm=int(input("enter a comm : "))
if esal>15000 and deptno==1 and comm!=0:
    esal=esal+5000
    print(eid,":::",ename,"   ",esal,"  ",deptno,"   ",comm)
else:
    print("the person is not eligible for increment")