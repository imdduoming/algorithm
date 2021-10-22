finding_target = 9
array = [0, 3, 5, 6, 1, 2, 4]
array.sort()
def is_exist_target_number_binary(target, numbers):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


result = is_exist_target_number_binary(finding_target, array)
print(result)