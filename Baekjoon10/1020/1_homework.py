input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime=[]
    for i in range(2,number):
        not_prime=0
        for j in range(2,i):
            if i%j==0:
                not_prime=1
                break
        if not_prime==0:
            prime.append(i)


    return prime


result = find_prime_list_under_number(input)
print(result)