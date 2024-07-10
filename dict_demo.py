emp={
    "eid":101,
    "ename":"balu",
    "esal":21000,
    "deptno":1
}
x=emp.get("ename")
print("value:::",x)
for i in emp.keys():
    print("keys::",i)
for v1 in emp.values():
    print("values:::",v1)
for k,v in emp.items():
    print("keys :::",k,"::values::",v)