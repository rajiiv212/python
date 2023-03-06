a = 125212
b=a
c=0
while(a>0):
    z=a%10
    c=c*10+z
    a=a//10
    print( z,c,a)
    
if(b==c):
    print("this is palindrom")
else:
    print("this is not palindrom")
