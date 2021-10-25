input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                array[i],array[j]=array[j],array[i]



    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!