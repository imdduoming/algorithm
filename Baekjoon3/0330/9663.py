#N-Queen
#백트래킹
import sys
input=sys.stdin.readline
N=int(input())

#열 배열 생성
col=[0]*(N+1)

def promising(x):
    for i in range(1,x):
        # 같은 행에 있는지 대각선 상에 있는지 확인
        if col[x]==col[i] or abs(col[x]-col[i])==(x-i):
            return False
    return True


def dfs(cnt):
    global result
    #열마다 1개씩 말을 놓는데 열이 N개 넘으면 경우의 수 1개 생성하고 종료
    if cnt>N:
        result+=1
        return

    # 종료조건에 해당되지 않으면 col[열]=행 을 해보며 유망한 후보인지 체크하고 유망하다면 재귀로
    else:
        for j in range(1,N+1):
            col[cnt]=j
            if promising(cnt):
                dfs(cnt+1)



result=0

dfs(1)
print(result)