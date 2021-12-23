#2019 상반기 LINE 인턴 채용 코딩테스트
from collections import deque
now_c=int(input())
b=int(input())

time=0
brown=deque()
brown.append((0,b))
visited = [{} for _ in range(200001)]

conny_d=0#conny가 움직이는 거리
flag=0
while now_c<200000:
    now_c+=time

# c의 위치 == b의 위치 비교 후 종료
    if time in visited[now_c]:
        break

    for i in range(0, len(brown)):
        now_btime,now_b=brown.popleft()


        if  0<now_b*2 and now_b*2<=200000 and now_btime+1 not in visited[now_b*2]:
            brown.append((now_btime+1,now_b*2))
            visited[now_b *2][now_btime+1] = True

        if  0<now_b+1 and now_b + 1 <= 200000  and now_btime+1 not in visited[now_b+1]:
            brown.append((now_btime + 1, now_b +1))
            visited[now_b + 1][now_btime+1] = True

        if 0 <= now_b -1  and now_b - 1 <= 200000 and  now_btime+1 not in visited[now_b-1]:
            brown.append((now_btime + 1, now_b -1))
            visited[now_b-1][now_btime+1] = True



    time+=1


print(time)



