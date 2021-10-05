#단어수학(골드4)
import sys
input=sys.stdin.readline
N=int(input())
words=[]
alpha=[0 for i in range(26)]
for i in range(N):
    str=input().rstrip()
    words.append(str)

for str in words:
    i=0
    while str:
        now=str[-1]
        alpha[ord(now)-ord('A')]+=pow(10,i)
        i+=1
        str=str[:-1]

alpha.sort(reverse=True)
ans=0
for i in range(9,0,-1):
    ans=ans+(i*alpha[9-i])

print(ans)



