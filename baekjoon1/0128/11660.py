import sys
input = sys.stdin.readline #빠른 입력
N, M = map(int, input().split())
nums=[[0 for col in range(N+1)] for row in range(N+1)]
pre=[[0 for col in range(N+1)] for row in range(N+1)]
for i in range(1,N+1):
    nums[i]=list(map(int,input().split()))

    for j in range(1,N+1):
         pre[i][j]=pre[i][j-1]+pre[i-1][j]-pre[i-1][j-1]+nums[i][j-1]
#print(pre[N][N])
sum=0
for i in range(0,M):
    x1,y1,x2,y2 = map(int, input().split())
    sum=0
    #print(pre[x2][y2])
    sum=pre[x2][y2]-pre[x1-1][y2]-pre[x2][y1-1]+pre[x1-1][y1-1]
    print(sum)
    '''
4 1
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
1 1 4 4
    
2 1
1 2
3 4
1 2 1 2
'''