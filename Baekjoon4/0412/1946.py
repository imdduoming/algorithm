#그리디알고리즘
#신입사원
#for문을 2번 돌릴 경우 최대 10만개의 데이터가 들어오기때문에 이 경우 걸리는 시간은 10만**2 이기 때문에 시간초과가 난다

import sys
input=sys.stdin.readline
T=int(input())

for i in range(T):
    N=int(input())
    score=[]
    for j in range(N):
        first,second=map(int,input().split())
        score.append((first,second))
    score.sort(key= lambda x:x[0])
    cnt=1
    min_score=score[0][1]
    for k in range(1,N):
        if score[k][1]<min_score:
            #서류성적 순으로 오름차순 정렬되어있기 때문에 현재까지의 가장 높은 면접성적을 min_score라는 변수에 저장
            #현재 순회하고 있는 면접점수가 min_score보다만 낮으면 선발될 수 있다
            min_score=score[k][1]
            cnt+=1
    print(cnt)