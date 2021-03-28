import numpy as np
ani=np.arange(6)
#print(ani)
#b=ani[ani%2==1]   #array_name[condition(or required array to print)]
#print(b)
#c=np.where(ani%2==1,-1,ani)    #to change/replace any element of array
#print(c)
#d=np.where(ani==2,0,ani)    #to change a specific element
#print(d)
ket=np.array([0,3,2,7,17,9])
#c=np.intersect1d(ani,ket)    #to find common elements b/w n arrays
#print(c)
#print(np.where(ani==ket))   #to print position of elemets which r common in both array
e=np.append(ani,[34,60,76])
print(e)
print(ani*ket)
