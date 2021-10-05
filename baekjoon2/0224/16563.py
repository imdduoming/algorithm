import sys
input=sys.stdin.readline
N=int(input())
nums=list(map(int,input().split()))
prime=[-1]*5000001
for i in range(2,5000001):
    prime[i]=i
for j in range(2,5000001*5000001):
    prime[i]=i
def solve(n):
    result=[True]*(n+1)
    m=int(n**0.5)

    for i in range (2,m+1):
        if result[i]==True:
            for j in range(i+i,n,i):
                result[j]=False
    ans=[i for i in range(2,n+1) if result[i]==True]
    return ans

for i in nums:
    prime=solve(i)
    while i>=2:
        for j in prime:
            if i%j==0:
                print(j,end=' ')
                break
        i=i/j
    print()

