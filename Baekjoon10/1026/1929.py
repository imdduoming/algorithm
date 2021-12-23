# 파이썬 1929 소수구하기
M,N=map(int,input().split())

def find_prime_list_under_number(M,N):
    # 이 부분을 채워보세요!
    prime={}
    for i in range(2,N+1):
        for j in range(i+i,N+1,i):
            if j not in prime:
                prime[j]=True
    return prime
answer=find_prime_list_under_number(M,N)

for i in range(M,N+1):

     if i!=1 and i not in answer:
         print(i)
