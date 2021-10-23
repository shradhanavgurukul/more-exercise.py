sentence= ["NavGurukul is an alternative to higher education reducing the barriers of current formal education system"]
a=[]
b=""
for i in sentence:
    if i=="":
        a.append(b)
        b=""
    b=b+i
if b==i:
    a.append(b)
print(a)
