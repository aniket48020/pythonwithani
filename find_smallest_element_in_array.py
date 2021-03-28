a=[]
n=int(input('no of terms'))
for i in range(1,n+1):
    b=input('element')
    a.append(b)
c=None
for i in a:
    if c is None:
        c=i
    elif(i<c):
        c=i
print(c)
