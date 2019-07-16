p=int(input())
r=[]
q=0
for i in range(0,p):
    r.append(i)
for j in range(len(r)):
    for k in range(j+1,len(r)):
        q+=1
print(q)
