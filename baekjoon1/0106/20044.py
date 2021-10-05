import sys
n = int(sys.stdin.readline())
level = list(map(int, input().split()))  #학생들의 역량
level=sorted(level)
team_score=[]
min_score=10000000
for i in range(0,n):
    team_score.append(level[i]+level[(2*n-1)-i])


print(min(team_score))