from calendar import c


a=int(input("enter the no."))
b=0
while(a>0):
    c=a%10
    b=b*10+c
    a=a//10
    print("revers",b ,c ,a)


