#문자열 알고리즘
#문자열폭발
#시간초과
import sys
import collections
input=sys.stdin.readline
str=input().strip()
bomb=list(input().strip())
m=len(bomb)
stack=[]
for i in str:
    stack.append(i)
    if i==bomb[-1]:
        if stack[-m:]==bomb:
            del stack[-m:]


'''
while str:
    if start_idx!=-1:
        end_idx=start_idx+len(bomb)-1
    else:
        break
    str=str[0:start_idx]+str[end_idx+1:]
#    print(str)
'''
if stack:
    print(*stack,sep="")
else:
    print("FRULA")
