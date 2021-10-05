import sys
input=sys.stdin.readline

#음수간선이 존재한다면 최솟값이 계속 갱신됨을 알 수 있다 무한히 갱신됨


TC=int(input())
for _ in range(TC):
    N,M,W=map(int,input().split())
    graph = []

    for _ in range(M): #도로 정보 입력받기
        S,E,T=map(int,input().split())
        graph.append([S,E,T])
        graph.append([E,S,T])

    for _ in range(W): #웜홀 정보 입력받기
        S,E,T=map(int,input().split())
        graph.append([S,E,-T])
    INF = sys.maxsize
    time = [INF for _ in range(N+1)]
    time[1] = 0
    for i in range(N):
        cycle=False
        # 출발노드를 제외한 모든 노드에 대해서 확인
        for j in range(2 * M + W):
            # 모든 간선을 확인 (다익스트라는 모든 간선을 확인하는 것이 아니라 특정 정점에 붙어있는 간선만 확인함)
            now = graph[j][0]
            next = graph[j][1]
            spend = graph[j][2]
            if time[now] != INF and time[next] > time[now] + spend:
                time[next] = time[now] + spend
                cycle=True
                if i == N - 1:
                    # n번째 라운드에서도 값이 갱신된다면 음수간선의 순환이 존재한다
                    cycle=True
                    break
        if cycle==False:
            break

    if cycle:
        print("YES")
    else:
        print("NO")
