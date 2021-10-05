import sys
N,M=sys.stdin.readline().split()
N=int(N)
M=int(M)

nums=[i+1 for i in range(N)]
visited=[False]*N
ans=[]
#백트래킹 알고리즘
def solve(level): #DFS
    if(level==M):
        print(*ans)
        return
    for i in range(0,N):
        #중복확인
        if (visited[i]==False):
            visited[i]=True
            ans.append(nums[i])
            solve(level+1)
            print(ans.pop())



            visited[i]=False
        else:
            continue


solve(0)