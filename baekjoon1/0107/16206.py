cake_num , max_cnt = input().split()  #주어진 케이크의 개수 cake_num과 자를 수 있는 최대횟수
max_cnt=int(max_cnt)
cake_num=int(cake_num)
cakes = list(map(int, input().split()))
cakes=sorted(cakes)
tens=[]
not_tens=[]
for i in range(0,cake_num):
    if(cakes[i] % 10 == 0):
        tens.append(cakes[i])
    else:
        not_tens.append(cakes[i])
new_cakes=tens+not_tens

count=0
cake_ten=0
break_flag = 0
for i in new_cakes:
    if(i==10):
        cake_ten+=1
    else:

        while(i>10):
            i=i-10
            count+=1
            cake_ten+=1
            if(i == 10):
                cake_ten+=1

            if (count == max_cnt):
                break_flag = 1
                break

    if(break_flag==1):
        break


print(cake_ten)
