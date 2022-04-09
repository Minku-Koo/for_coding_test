#union find알고리즘 활용 
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    parent[y] = x

node = int(input())
edge = int(input())

parent = []
for i in range(0,node+1):
    parent.append(i)

for _ in range(edge):
    a,b = map(int,input().split())
    union(a,b)

cnt = 0
computer = find(1)
for i in range(1,len(parent)):
    if find(i) == computer:
        cnt+=1
print(cnt-1)