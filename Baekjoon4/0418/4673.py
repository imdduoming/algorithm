#구현알고리즘
#셀프넘버
sum=0
result={}
for num in range(1,10001):

    while True:
        sum=0
        if num>10000:
            break
        num=str(num)
        for i in num:
            sum=sum+int(i)
        sum=sum+int(num)
        if sum>10000:
            break
#        print('sum:',sum)

        if sum not in result:
            result[sum]=0
        num=sum


#print(result)

for i in range(1,10001):
    if i not in result:
        print(i)
