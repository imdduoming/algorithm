#스텍 큐 덱
import sys
input = sys.stdin.readline #빠른 입력

table={')':'(',']':'[','}':'{'}
while True:
    str=input()
    #print(str)
    stack=[]
    ans_flag=0 #안되면 1로
    if str == '.':
        break

    for i in str:
        if i=='(' or  i=='{' or  i=='[' or i==']' or i==')' or i=='}':


            if i not in table:
                stack.append(i)
            elif not stack or (table[i] != stack.pop()):
                ans_flag=1
                break


    if (ans_flag==0) and len(stack)==0:
        print('yes')
    else:
        print('no')









