def factorial(n):
    #특정숫자로 떨어지는 조건
    if n==1:
        return 1
    return n*factorial(n-1)


print(factorial(5))