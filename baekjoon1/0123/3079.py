import sys
N,M=sys.stdin.readline().split()
N=int(N)
M=int(M)
arr=[]
for i in range(N):
    arr.append(int(sys.stdin.readline()))
ans=0
left=min(arr)
right=max(arr)*M
while left<=right:
    total=0 #mid시간동인 검사할 수 있는 총 사람의 수
    mid=(left+right)//2
    for i in range(N):
        total+=mid//arr[i] #mid시간동안 검사할 수 있는 사ㅏㄻ의 수
        if total==M:
            ans=mid
            break
    if total >= M:
        ans=mid
        right=mid-1
    else:
        left=mid+1



print(ans)