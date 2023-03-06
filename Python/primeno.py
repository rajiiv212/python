n=100
for i in range(0,n):
    c=0
    for j in range(2,i/2):
        if i%j==0:
            c=c+1
        if c==0 and j!=1:
                print(i)