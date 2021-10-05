import sys
input = sys.stdin.readline #빠른 입력
G= int(input())
nums=[] # G의 약수들
for i in range(1,G+1):
    if G%i==0:
        nums.append(i)

ans=[]
x=0
y=0
sum=0
val=0
for i in nums:
    x=i
    y=G/i
    sum=x+y
    if (sum) %2==0:
        val=int(sum/2)
        if i-val>0:
            ans.append(int(sum/2))

if len(ans)==0:
    print(-1)
else:
    ans=sorted(ans)
    for i in ans:
        print(i)

