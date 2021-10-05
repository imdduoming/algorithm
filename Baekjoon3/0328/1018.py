import sys
N,M=map(int,input().split())
chess=[]


for i in range(N):
    row=list(input().rstrip())
    chess.append(row)
result=0
ans=1000000
for i in range(0,N-7):
    for j in range(0,M-7):
        case1 = 0  # 맨위가 white인 경우
        case2 = 0  # 맨 위가 black 인 경우
        for a in range(i,i+8):
            for b in range(j,j+8):
                if chess[a][b] == 'W':
                    # 순회하는 체스판이 흰색일경우 case1 의 경우는 짝수 , case2의 경우는 홀수여야함
                    if (a + b) % 2 == 0:
                        # case2가 되기 위해서는 case2 기회비용 추가
                        case2 += 1

                    else:
                        # case2가 되기 위해서는 case2 기회비용 추가

                        case1 += 1
                else:

                    if (a + b) % 2 == 0:
                        case1 += 1
                    else:
                        case2 += 1

        result=min(case2,case1)
#        print('result:',result)
        ans=min(ans,result)
 #       print('ans:',ans)
print(ans)


