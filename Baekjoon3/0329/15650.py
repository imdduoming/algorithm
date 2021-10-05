import sys
input=sys.stdin.readline
N,M=map(int,input().split())
arr=[i for i in range(1,N+1)]
def solve(new_arr,cnt,visited):
    if cnt==M and sorted(new_arr)==new_arr:
        print(*new_arr)
        return
    else:
        for i in arr:
            if visited[i]!=True:
                new_arr.append(i)
                visited[i]=True
                #print('i:',i,'cnt:',cnt,'new_arr',new_arr)
                solve(new_arr,cnt+1,visited)
                visited[i] = False
                new_arr.pop()
                #print('i:',i,'cnt:',cnt,'visited:',visited)
                #print('pop된 후 new_arr',new_arr)


for i in range(1,N+1):
    cnt=1
    visited=[0]*(N+1)
    visited[i]=True
    new_arr=[i]
    solve(new_arr,1,visited)