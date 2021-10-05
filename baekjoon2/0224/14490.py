#유클리드호제법 (최대공약수 구하기)
import sys
input=sys.stdin.readline
N,M=map(int,input().split(':'))
def gcd(a,b):
    while b!=0:
        d=a%b
        a=b
        b=d
    return a

num=gcd(N,M)
print('%d:%d'%(N//num,M//num))