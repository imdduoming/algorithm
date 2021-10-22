#문자열뒤집기
input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    flag_1=0
    flag_0=0
    count_0=0
    count_1=0
    for i in string:
        if i=='0':
            if flag_0==0:
                flag_0=1
                count_0+=1
                flag_1=0
        else:
            if flag_1==0:
                flag_1 = 1
                count_1 += 1
                flag_0 = 0

    return min(count_0,count_1)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)