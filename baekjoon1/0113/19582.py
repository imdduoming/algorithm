import sys
N=int(sys.stdin.readline())
contest=[]

for i in range(0,N):
    arr= list(map(int, sys.stdin.readline().split()))
    contest.append(arr)

money=0 #누적된 상else금
max_money=0
cont_count=N   #참여할 수 있는 대회 갯수
for i,j in contest:
    if(money<=i):
        money=money+j
        if(max_money<j):
            max_money=j
    elif (money-max_money>i or max_money<j): #이번 대회 skip해야함
        cont_count-=1
    else:
        money=money-max_money
        money+=j
        cont_count-=1

if(cont_count<N-1):
    print('Zzz')
else:
    print('Kkeo-eok')