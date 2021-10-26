N=int(input())

def check(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True
for i in range(N):
    if check(input()):
        print('YES')
    else:
        print('NO')