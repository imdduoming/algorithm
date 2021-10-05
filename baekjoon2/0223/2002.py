import sys
import collections
imput=sys.stdin.readline
N=int(input())
enter={}
out={}

count=0
for i in range(N):
    car=input().rstrip()
    enter[car]=i
for i in range(N):
    car=input().rstrip()
    out[i]=car
for i in range(0,N):
    for j in range(i,N):
        if enter[out[i]]>enter[out[j]]:
            count+=1
            break
print(count)



