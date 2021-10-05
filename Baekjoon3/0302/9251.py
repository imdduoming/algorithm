import sys
input=sys.stdin.readline
str=list(input().rstrip())
str2=list(input().rstrip())
str=[0]+str
str2=[0]+str2

lenstr=len(str)
lenstr2=len(str2)

#print(str)
#print(str2)
dp=[[0 for i in range(lenstr2)] for j in range(lenstr)]
for i in range(1,lenstr):
    for j in range(1,lenstr2):
        if str[i]==str2[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[lenstr-1][lenstr2-1])



