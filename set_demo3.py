s1={"AWS","murali","balu","azhar","hello"}
s2={"azhar","AWS"}
s3=s1.intersection(s2)
print(s3)
s4=s1 & s2
print(s4)

s1.intersection_update(s2)
print(s1)
