p=int(input())
num2=list(map(int,input().split()))
l1=[]
for i in num2:
    if num2.count(i)>1:
        if str(i) not in l1:
            l1.append(str(i))
if len(l1)==0:
    print("unique")
else:
    num2.sort()
    print(" ".join(l1))
