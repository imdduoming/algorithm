import sys
input=sys.stdin.readline
N=int(input())
wait=list(map(int,input().split()))
wait.sort()
time=[0]*N
total=0
for i in range(0,len(wait)):
    total=0
    for j in range(0,i):
        total+=wait[j]
    time[i]=total+wait[i]


print(sum(time))