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
for i in nums:
    x=(i+(G/i))/2 #현재몸무게
    #print(x)
    y=i-x
    if (i+G/i)%2==0:
        if x>0 and y>0 :
            ans.append(int(x))
if len(ans)==0:
    print(-1)
else:
    ans=sorted(ans)
    for i in ans:
        print(i)
