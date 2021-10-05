#그리디알고리즘
#수묶기
import sys
input=sys.stdin.readline
N=int(input())
nums=[]
for i in range(N):
    nums.append(int(input()))

#print(nums)
sum=0
nums.sort(reverse=True)
total=0

i=0
while True:
    if not nums:
        break
    if len(nums)==1:
        total=total+nums[0]
        break
    #수가 2개 이상일 때
    if nums[0]>0: #조회하고 있는 숫자가 양수일때
        if nums[1]>0: #그 다음숫자도 양수라면
            #둘다 1보다 큰 양수라면
            if nums[0]>1 and nums[1]>1:
                sum=nums[0]*nums[1]
                total=total+sum



            else:
            #둘다 0이거나 1이라면
                total=total+nums[0]
                total=total+nums[1]
            nums.pop(0)
            nums.pop(0)
        else:
            #그다음 숫자가 음수라면
            total=total+nums[0]
            nums.pop(0)
    else:
        #조회하고 있는 숫자가 0또는 음수라면

         while len(nums)>1:
                sum=nums[len(nums)-1]*nums[len(nums)-2]
                nums.pop()
                nums.pop()
                total=total+sum

#    print('i:', i, 'total:', total)
 #   print('nums:',nums)

print(total)