import sys
input= sys.stdin.readline
board=[]
for i in range(9):
    row=list(map(int,input().split()))
    board.append(row)

zeros=[]
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            zeros.append((i,j))

def is_promising(i,j): #zeros[i][j]에 들어갈 유망한 숫자 찾기
    promising=[1,2,3,4,5,6,7,8,9]

    #행열검사
    for k in range(9):
        if board[i][k] in promising:
            promising.remove(board[i][k])
        if board[k][j] in promising:
            promising.remove(board[k][j])

    i//=3 #i를 3으로 나눈 몫
    j//=3 #j를 3으로 나눈 몫
    #3*3 박스 검사
    for a in range(i*3,(i+1)*3):
        for b in range(j*3,(j+1)*3):
            if board[a][b] in promising:
                promising.remove(board[a][b])

    #가로 세로 3*3 박스 에 들어있는 숫자 다 제외하고 최종 유망한 숫자만 반환
    return promising

#ans_flag=False # 답이 출력되었는가

def dfs(n):
 #   global ans_flag

    if n==len(zeros):
        for row in board:
            print(*row)
        sys.exit(0)
    else:
        (i,j)=zeros[n]
        promising=is_promising(i,j)
  #      print('i:',i,'j:',j,'유망한 후보군:',promising)

        for num in promising:
            #유망한 숫자 후보들 중 하나를 넣어봄
   #         print(num)
            board[i][j]=num
            #다음 0으로 넘어감
            dfs(n+1)

            board[i][j]=0
            '''
            num 으로 설정하고 위 dfs(n+1)함수를 호출했을 때 유망한 숫자가 없이 그냥 종료된다면  
            board[i][j]의 값은 num이 아니므로 0으로 바꾸고 유망한 후보군 중 다음 후보를 순회해야한다
            '''
dfs(0)

