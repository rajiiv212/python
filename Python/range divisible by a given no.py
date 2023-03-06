lower= int(input("enter the lower no."))
upper= int(input("enter the upper no."))
n=int(input("enter the civide no."))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)

