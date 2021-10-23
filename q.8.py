list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
i=0
b=[]
while i<len(list2):
    k=list1[i]
    if k not in b:
        b.append(k)
    i=i+1
print(b)