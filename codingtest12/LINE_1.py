#2019 상반기 LINE 인턴 채용 코딩테스트
from collections import deque
c=int(input())
b=int(input())
conny=[]
conny.append(c)
time=0
brown=deque()
brown.append((0,b))
visited = [{} for _ in range(200001)]

conny_d=0#conny가 움직이는 거리
flag=0
while True:

    now_c=conny.pop()

    if now_c>200000:
        break

    while brown:
        now_btime,now_b=brown.popleft()

        if time!=now_btime:
            brown.appendleft((now_btime,now_b))
            break
        if now_b==now_c:
            flag=1
            break


        else:
            if 0<= now_b*2 and now_b*2<=200000 and now_btime not in visited[now_b*2]:
                brown.append((now_btime+1,now_b*2))
                visited[now_b *2][now_btime] = True
            if 0 <= now_b + 1 and now_b + 1 <= 200000  and now_btime not in visited[now_b+1]:
                brown.append((now_btime + 1, now_b +1))
                visited[now_b + 1][now_btime] = True
            if 0 <= now_b -1  and now_b -1 <= 200000 and  now_btime not in visited[now_b-1]:
                brown.append((now_btime + 1, now_b -1))
                visited[now_b-1][now_btime] = True

    if flag==1:
        break

    time+=1
    conny_d+=1
    conny.append(now_c+conny_d)




print(time)



