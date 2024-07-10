s1={"apple","gopi","hari"}
s2={"aws","azure","apple"}
s3=s1.difference(s2)
print(s3)
s4={"nani","suma","apple"}
s5=s1.difference(s2,s4)
print(s5)
#how use - in between 3 obj
s6=s1-s2-s4 #-->s1-s2 , s1-s4
print(s6)
#how to change original set
s1.difference_update(s2)
print("compare two set :::",s1)
s1.difference_update(s2,s4)
print("compare three set :::",s1)
s1 -= s2
s1 -= s4
print("compare 3 set with -=:::",s1)
s10={"pavan","roja","ravi"}
s11={"pavan","rao","arora"}
s13={"pavan","chiru","ntr"}

#symmetric object 
s12=s10.symmetric_difference(s11)
print("symmetric obj:::",s12)
s14=s10.symmetric_difference(s11).symmetric_difference(s13)
print("compare 3 obj",s14)
s15=s10 ^ s11 ^ s13
print("compare 3 objs",s15)
s10.symmetric_difference_update(s11)
print("symmetric_difference_update::",s10)