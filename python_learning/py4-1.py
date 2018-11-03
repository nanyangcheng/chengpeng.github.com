for x in range(1,21):
     print(x)
y = 0
print(y)
long=list(range(1,1000000))
for x in long:
    y=x+y
print(y)
longs=list(range(1,20,2))
for x in longs:
    print(x)
liebiao=[z**3 for z in range(1,11) ]
print(liebiao)
print(liebiao[-3:])
print(liebiao[1:3])
xx=liebiao[:]
print(xx)
liebiao.append(8)
xx.append(9)
print(liebiao)
print(xx)
         
    