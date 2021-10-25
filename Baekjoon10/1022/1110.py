#백준 1110 번 while 문 알고리즘
# 더하기사이클
N=int(input())

def cycle_count(N):

    if N<10:
        one=N
        new_N=N*10+one

    else:
        ten=N%10
        one=N//10+N%10
        one = one % 10
        new_N=ten*10+one

    count=1
    while new_N!=N:
        if new_N < 10:
            one = new_N
            new_N = new_N * 10 + one

        else:
            ten = new_N % 10
            one = new_N // 10 + new_N % 10
            one = one%10
            new_N = ten * 10 + one
        count+=1


    return count


print(cycle_count(N))