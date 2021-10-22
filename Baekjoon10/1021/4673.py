#알고리즘 - 함수
#백준 4673 셀프넘버
not_result={}
for a in range(1,10001):
    str_a=list(str(a))
    str_a=[int(a) for a in str_a]
    sum_a=sum(str_a)
    not_result[sum_a+a]=1

for a in range(1,10001):
    if a not in not_result:
        print(a)


