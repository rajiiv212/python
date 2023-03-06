
n=int(input("enter the no."))
a=[]
for i in range (0 ,n):
     Element=int(input("enter the no. "))
     a.append(Element)
avg=sum(a)/n
print("Average of element in the list",round(avg,2))
