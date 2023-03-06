l=[]
for i in range(150,250):
    if i%5==0:
        l.append(i)
        print(i,end="+ ")
sum=0
for j in l:
    sum= sum +i

print("=",sum)