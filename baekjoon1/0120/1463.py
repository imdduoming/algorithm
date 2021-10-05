import sys
N=int(sys.stdin.readline())
dp=[0]*10000012
dp[0]=0
dp[1]=0
dp[2]=1
dp[3]=1
for i in range(4,1000001):
    divide_three=sys.maxsize
    divide_two=sys.maxsize
    minus_one=sys.maxsize
    min_divide=sys.maxsize
    if i%3==0:
        divide_three=dp[i//3]+1
    if i%2==0:
        divide_two=dp[i//2]+1
    minus_one=dp[i-1]+1
    min_divide=min(divide_two,divide_three)
    dp[i]=min(min_divide,minus_one)

print(dp[N])