#주유소
#그리디 알고리즘
import sys
input=sys.stdin.readline
N=int(input())

dist=list(map(int,input().split()))
price=list(map(int,input().split()))


total=0
min_price=price[0]
for i in range(0,len(dist)):
    if min_price>=price[i]:
        min_price=price[i]
    total+=dist[i]*min_price

print(total)

