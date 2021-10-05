import sys
input=sys.stdin.readline
N=int(input())
schedule=[]
for i in range(N):
    start,end=map(int,input().split())
    schedule.append((start,end))
schedule.sort(key=lambda x:(x[1],x[0]))

# 시작시간과 끝나는시간이 같은 회의가 있을 수도 있기 때문에 끝나는시간 ,시작하는 시간으로 2번정렬해준다
#print(schedule)

count=1
end_time=schedule[0][1]
for a in range(1,len(schedule)):
    start=schedule[a][0]
    end=schedule[a][1]
    if start>=end_time:
        end_time=end
        count+=1
        #print('end_time:',end_time)

print(count)