n=int(input())
num1=list(map(int,input().split()))
l1=[]
for i in num1:
    if num1.count(i)>1:
        if str(i) not in l1:
            l1.append(str(i))
if len(l1)==0:
    print("unique")
else:
    num1.sort()
    print(" ".join(l1))
