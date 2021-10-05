import sys
n = int(sys.stdin.readline())
level = []
for i in range(n):
    num = int(sys.stdin.readline())
    level.append(num)
count = 0
for i in range(n-2,-1,-1):
    if(level[i]>=level[i+1]):
        while(level[i]>=level[i+1]):
            level[i] -= 1
            count += 1
            print(i,',',level[i])


print(count)
'''
4
9
8
7
5
'''


