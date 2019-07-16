o=int(input())
p=list(map(int,input().split()))
q=[]
for l in p:
  if(p.count(l)<2):
    if l not in q:
      q.append(l)
print(*q)
