import sys
import collections
input=sys.stdin.readline
N=int(input())
K=int(input())
board=[[0 for i in range(N+1)] for j in range(N+1)]
#print(board)
for i in range(K):
    col,row=map (int,input().split())
    board[col][row]=1

L=int(input()) #뱀의 방향 변환 횟수L
move=collections.deque()
for i in range(L):
    second,direct= input().split()
    move.append((int(second),direct))

now=0
dy=[0,0,1,-1]
dx=[1,-1,0,0]







