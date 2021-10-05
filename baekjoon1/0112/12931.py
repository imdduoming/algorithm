import sys
N=int(sys.stdin.readline())
arrB= list(map(int, input().split()))
count=0


while True:

    for i in range(0,N):
        if(arrB[i]%2!=0):
            arrB[i]=arrB[i]-1
            count+=1
    print(arrB, count)
    if sum(arrB) == 0:
        break
    for i in range(0,N):
        arrB[i]=arrB[i]//2

    count+=1



print(count)