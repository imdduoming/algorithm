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
            solve(level + 1)

            ans.pop()

            for j in range(i+1,N):
                visited[j] = False

            print(ans)
        else:
            continue

solve(0)


'''
1 2 3 4 5
[1, 2, 3, 4]
[1, 2, 3]
[1, 2, 3, 5]
[1, 2, 3]
[1, 2]
[1, 2, 4]
[1, 2, 4, 5]
[1, 2, 4]
[1, 2]
[1, 2, 5]
[1, 2, 5]
[1, 2]
[1]
[1, 3]
[1, 3, 4]
[1, 3, 4, 5]
[1, 3, 4]
[1, 3]
[1, 3, 5]
[1, 3, 5]
[1, 3]
[1]
[1, 4]
[1, 4]
[1, 4, 5]
[1, 4, 5]
[1, 4]
[1]
[1, 5]
[1, 5]
[1, 5]
[1]
[]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4]
[2, 3]
[2, 3, 5]
[2, 3, 5]
[2, 3]
[2]
[2, 4]
[2, 4]
[2, 4, 5]
[2, 4, 5]
[2, 4]
[2]
[2, 5]
[2, 5]
[2, 5]
[2]
[]
[3]
[3]
[3, 4]
[3, 4]
[3, 4, 5]
[3, 4, 5]
[3, 4]
[3]
[3, 5]
[3, 5]
[3, 5]
[3]
[]
[4]
[4]
[4]
[4, 5]
[4, 5]
[4, 5]
[4]
[]
[5]
[5]
[5]
[5]
[]
'''