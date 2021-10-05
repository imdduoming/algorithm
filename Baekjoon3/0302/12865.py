#다이나믹 프로그래밍 냅색문제 0-1냅색  

import sys
input=sys.stdin.readline
N,M=map(int,input().split())
cargo=[[0,0]]
for i in range(N):
    weight,val=map(int,input().split())
    cargo.append([weight,val])

#print('cargo:',cargo)
pack = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1,N+1):
    for curr_weight in range(1,M+1):
        if curr_weight<cargo[i][0]:
        #현재가방수용량이 담으려고 하는 짐의 무게보다 작으면 위의 값을 그대로 가져옴
            pack[i][curr_weight]=pack[i-1][curr_weight]
        else:
            #현재물건 담을 수 있는 경우
            pack[i][curr_weight]=max(cargo[i][1]+pack[i-1][curr_weight-cargo[i][0]],pack[i-1][curr_weight])
#print(pack)
print(pack[N][M])
