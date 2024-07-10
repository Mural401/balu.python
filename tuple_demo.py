#t=("hello",10,True,False,15.0)
#print(t,"datatype:::",type(t))

#l1=list(t)
#l1[0]="bye"
#print("after manipulating :::",l1)
#for x in t:
    #print(x)


t3=("balu","murali","yuvi")
(x,y,z)=t3
print ("x value ::",x)
print ("y value ::",y)
print ("z value ::",z)

t4=("balu","murali","yuvi","raju","krishna")
(n1,n2,*n3)=t4
print ("n1 value ::",n1)
print ("n2 value ::",n2)
print ("n3 value ::",n3)

t5=("balu","murali","yuvi","raju","krishna")
l3=list(t5)
print(l3[0:2])
print(l3[2:3])
print(l3[4])


