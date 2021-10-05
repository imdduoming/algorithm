import sys

input = sys.stdin.readline #빠른 입력
N,K=map(int, input().split())

stack=[]
for i in range(1,N+1):
    stack.append(i)
newArr=[]
idx=0
for k in range(N):
    idx=idx+K-1
    if(idx>=len(stack)):
        idx=idx%len(stack)
    newArr.append(str(stack.pop(idx)))
#print("<",", ".join(newArr)[:],">", sep='')

for i in range(0,len(newArr)):
    if(i==0):
        print("<",newArr[i],end=', ')
    elif(i==len(newArr)-1):
        print(newArr[i],'>')
    else:
        print(newArr[i],end=', ')

#<3, 6, 2, 7, 5, 1, 4>
#< 3, 6, 2, 7, 5, 1, 4 >