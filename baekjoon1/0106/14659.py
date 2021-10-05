import sys
n = int(sys.stdin.readline())

mountain = list(map(int, input().split()))
max = 0
cnt=0
max_cnt = 0
for i in range(n):
    if mountain[i]>max:
        max = mountain[i]
        cnt = 0
    else:
        cnt += 1
        if(max_cnt<cnt):
            max_cnt=cnt

print(max_cnt)
