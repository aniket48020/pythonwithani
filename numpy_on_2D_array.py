import numpy as np
ani=np.array([[1,2,3],[3,2,1]])
print(ani)
#print(ani.reshape(3,2))        #(row,column)
#print(ani.transpose())
#b=np.tile(ani,4)     #to make n no of copy
#print(b)
#c=np.tile(ani,[3,2])    # [x,y]  or reps=[x,y]
#print(c)
ket=np.array([[2,4,6],[1,3,67]])
d=np.concatenate((ani,ket),axis=1)    #to add/merge 2 array (axis=1:=add along y-axis)
print(d)
print(ani+ket)
print(ani/ket)
print(ani.astype(float))     #to convert int array to float
