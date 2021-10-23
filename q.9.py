num=int(input("enter the number"))
n=num
rem=0
sum=0
while num>100:
    rem=num%10
    sum=sum+rem
    num=num//10
if n%sum==0:
    print(n,"is a harashad number")
else:
    print(n,"is not a harashad number")