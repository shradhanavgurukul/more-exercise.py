list1=[1,342,75,23,98]
list2=[75,23,98,12,78,10,1]
b=[]
i=0
while i<len(list2):
    k=list2[i]
    if k in list1:
        b.append(k)
    i=i+1
print(b)


