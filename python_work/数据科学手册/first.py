import array
import numpy as np
L = list(range(10))
print(type(L[0]))
L2 = [str(c) for c in L]
print(L2)
L3 = ['2',True,3.0,4]
L4 = [type(item) for item in L3]
print(L4)

L5=list(range(10))
A = array.array('i',L5)
print(A)
print(np.array([1,4,5,8,9]))
print(array)

c = np.array([1,2,3,5],dtype='float32')
print(c)

h = np.array([range(i,i+3) for i in [2,4,6]])
print(h)

print(np.empty(3))
print(         )

x1 = np.random.randint(10,size=6)
x2 = np.random.randint(10,size=(3,4))
x3 = np.random.randint(10,size=(3,4,5))
print(x3.dtype)

x=np.arange(10)
print(x)
a = x[:5]
print(a)

b = x[::2]
print(b)

c = x[2::3]
print(c)

d = x[5::-2]
print(d)

f = 


















	
