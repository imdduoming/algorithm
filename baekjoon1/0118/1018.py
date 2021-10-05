import sys
N,M=sys.stdin.readline().split()
N=int(N)
M=int(M)

answer=10000


arr = [list(input()) for _ in range(N)]
comp=0
for a in range(0,N-7):
    for b in range(0,M-7):
        case1 = 0  # 맨위가 블랙
        case2 = 0  # 맨위가 화이트

        for i in range(a,a+8):
            for j in range(b,b+8):
                if arr[i][j]=='W':
                    if((i+j)%2==0):
                        case1+=1
                    else:
                        case2+=1
                else:
                    if ((i + j) % 2 == 0):
                        case2 += 1
                    else:
                        case1 += 1
        comp=min(case1,case2)

        answer=min(answer,comp)

print(answer)