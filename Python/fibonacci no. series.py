n=10
fact=0
a=1
print("fibonacci series: 0 1",end=" ")
for i in range(2,n):
    n=fact+a
    fact=a
    a=n
    print(n,end=" ")
