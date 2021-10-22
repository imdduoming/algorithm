#반복되지 않는 첫번째  문자
input = "abacabade"


def find_not_repeating_character(string):
    str_dict={}
    for i in string:
        if i not in str_dict:
            str_dict[i]=1
        else:
            str_dict[i]+=1

    for key in str_dict:
        if str_dict[key]==1:
            one=key
            break

    return one


result = find_not_repeating_character(input)
print(result)