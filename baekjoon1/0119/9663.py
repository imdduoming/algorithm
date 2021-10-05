n = int(input())
s = [0 for i in range(16)]
result = 0


def check(x): #가로 세로 대각선 확인
    for i in range(1, x):
        if s[x] == s[i] or abs(s[x] - s[i]) == x - i:
            return False
    return True


def dfs(col):
    global result
    if col > n:
        result += 1
    else:
        for i in range(1, n + 1):
            s[col] = i
            if check(col):
                dfs(col + 1)


dfs(1)
print(result)