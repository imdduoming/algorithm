s = "(()()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    stack=[]
    for i in string:
        if i=='(':
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


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!