import sys
N=int(sys.stdin.readline())
break_flag=0
for i in range(1,N+1):
    divide_nums=list(map(int,str(i)))
    sum_nums=i+sum(divide_nums)
    if(sum_nums==N):
        break_flag=i
        break
print(break_flag)