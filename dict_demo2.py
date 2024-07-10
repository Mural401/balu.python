stu={
    "sid":111,
    "sname":"Murali",
    "ssources":["java","python"],
    "saddress":"Hyd"
}
r1=stu.popitem()
print("after remove last from dict:::",r1)
del stu["sname"]
print("after remove sname from dict::",stu)
