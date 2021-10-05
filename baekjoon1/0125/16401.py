import sys
N,M=map(int,sys.stdin.readline().split())
snack=list(map(int,sys.stdin.readline().split()))
snack=sorted(snack)


left=1
right=snack[-1]
snack_length=0#과자의길이
while left <= right :
    mid= (left + right)//2


    total=0

    for i in range(0,len(snack)):
       total+=snack[i]//mid
#    print('total: ',total)

    if total>=N:
        if total==N:
            snack_length=max(snack_length,mid)

        left=mid+1
    else:
        right=mid-1

print(snack_length)