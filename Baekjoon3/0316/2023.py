import sys
import collections
import math
input=sys.stdin.readline
N=int(input())

#1은 소수가 아니기 때문에 1이 맨 앞으로 올 수는 없음
def is_prime(n):
#소수인지 판별하는 함수 에라토스테네스의 체
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: #소수인경우
            return False
    return True




ans=[]

def dfs(cnt,num):

    if cnt==N: #자릿수가 cnt와 같아지면
        print(num)


    for i in range(1,10,2):
        tmp=num*10+i
        if is_prime(tmp):
            dfs(cnt+1,tmp)




prime=[2,3,5,7]
for i in range(0,4):
    dfs(1,prime[i])
