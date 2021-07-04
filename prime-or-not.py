n=int(input("enter the number"))
bool=True
if(n==1 or n==2):
    print(n," is not prime")
else:
    for i in range(2, n):
        if(n%i==0):
            print(n," is not prime")
            bool=False
            break
    if(bool==True):
        print(n," is prime")