#잃어버린 괄호
#그리디 알고리즘
import sys
import re
input=sys.stdin.readline
str=input().split('-')
num=[]

for i in str:
    cnt=0
    s=i.split('+')
    for j in s:
        cnt+=int(j)
    num.append(cnt)

first=num[0]
for i in range(1,len(num)):
    first=first-num[i]
print(first)


'''
giho=[]
num=[]
for i in str:
    if i=='+':

print(giho)
for i in giho:


'''