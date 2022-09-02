a=[1,3,5]
b=[2,4,6]
c=[]

for i in a:
    c.append(i)
    
for i in range(len(b)):
    c[i]=b[i]+c[i]
    

print(c)