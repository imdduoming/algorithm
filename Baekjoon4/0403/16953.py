import sys
input=sys.stdin.readline
A,B=map(int,input().split())
cnt=0
able=0 #연산가능 ?
while True:

    str_B=str(B)
    if B==A:
        able=1
        break
    if B<A:
        print(-1)
        break

    if B%2==0:
        B=B//2
        cnt+=1
        #print('B:',B,'cnt:',cnt)
    elif str_B[-1]=='1':
        str_B=str_B[:-1]
        cnt+=1
        B=int(str_B)
        #print('B:', B, 'cnt:', cnt)
    else:
        print(-1)
        break

if able==1:
    print(cnt+1)