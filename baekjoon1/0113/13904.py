import sys
N=int(sys.stdin.readline())
homework=[]

for i in range(0,N):
    arr= list(map(int, input().split()))
    homework.append(arr)

homework.sort(key=lambda x:x[1],reverse=True)

schedule={}
for i ,j in homework:
    idx=i
    while(idx>=1):
        if(idx not in schedule): #schedule의 index 0은 비워둔다
            schedule[idx]=j
            break
        else:
            idx-=1
total=0
for val in schedule.values():
    total+=val



print(total)