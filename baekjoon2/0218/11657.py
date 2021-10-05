#벨만포드 알고리즘
#음수간선이 존재하고 순환
#다익스트라와 벨만포드 알고리즘 정리해서 오늘밤 블로그 업뎃하기
import sys
input=sys.stdin.readline
INF=int(10**9)
N,M=map(int,input().split())
edge=[] #간선에 대한 정보를 담는 리스트
for i in range(M):
    A,B,C=map(int,input().split())
    edge.append((A,B,C))
distance=[INF]*(N+1)
distance[1]=0
negative_flag=0
for i in range(N):
    #정점마다 모든 간선을 확인
    for j in range(M):
        now=edge[j][0]
        next=edge[j][1]
        cost=edge[j][2]
        if distance[now]!=INF and distance[next]>distance[now]+cost:
            #현재간선을 거쳐 다음노드로 이동하는 거리가 더 짧은 경우
            distance[next]=distance[now]+cost
            #정점마다 n-1번 간선확인작업을 반복해야하는데 마지막에 이 과정을 한번 더 수행하여 음수간선순환이 발생하여 최단거리 테이블이 갱신된다면
            #음수간선순환이 존재되는것임
            if i==N-1:
                negative_flag=1

if negative_flag==1:
    print(-1)
else:
    for i in range(2,N+1):
        if distance[i]!=INF:
            print(distance[i])
        else:
            print(-1)





