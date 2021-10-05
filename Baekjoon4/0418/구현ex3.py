#동빈나 이코테
#구현 문제3 문자열재정렬
import sys
S=sys.stdin.readline()
count=0
str=[]
for i in S:
    if i.isdigit():
        count+=int(i)
    else:
        str.append(i)
str.sort()
str.append(count)
for i in str:
    print(i,end='')
print()
#K1KA5CB7