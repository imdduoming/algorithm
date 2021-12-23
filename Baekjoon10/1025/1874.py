N=int(input())

stack=[]
num=1
answer=[]
no_flag=0
for i in range(N):
    now=int(input())
    while num<=now:
        stack.append(num)
        answer.append('+')
        num += 1

    if now==stack[-1]:

        stack.pop()
        answer.append('-')

    else:
        no_flag=1

if no_flag:
    print('NO')
else:
    for i in answer:
        print(i)







