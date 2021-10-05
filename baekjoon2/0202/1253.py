import sys
input=sys.stdin.readline
N=int(input())

num_Arr=list(map(int,input().split()))
num_Arr=sorted(num_Arr)

count=0
for i in range(len(num_Arr)-1,-1,-1):
    nums=num_Arr[:i]+num_Arr[i+1:]
    left = 0  # index 2부터
    right = len(nums)-1

    while left<right:
        if nums[left]+nums[right]<num_Arr[i]:
            left+=1
        elif nums[left]+nums[right]>num_Arr[i]:
            right-=1
        elif nums[left]+nums[right]==num_Arr[i]:
            count+=1
            break


print(count)


    

