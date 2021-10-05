# 스택 큐
import sys

input = sys.stdin.readline #빠른 입력
N=int(input())
str=input().rstrip()
stack=[]
nums = []
for i in range(N):
    a=int(input())

    nums.append(a)

for i in str:
    if i.isalpha():
        #print(stack)
        stack.append(nums[ord(i)-ord('A') ])

    else:
        a = stack.pop()
        b = stack.pop()
        if(i=='*'):
            sum=b*a

        if (i == '+'):
            sum = b + a
        if (i == '-'):
            sum = b - a
        if (i == '/'):
            sum = b / a

        stack.append(sum)

print('%.2f' %stack.pop())
