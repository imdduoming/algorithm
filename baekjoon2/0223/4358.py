import sys
import operator
import collections
input=sys.stdin.readline
arr=[]
arr_dict={}
count=0
while True:
    strs=input().rstrip()
    if not strs:
        break
    count+=1


    arr.append(strs)
arr_dict=collections.Counter(arr)

arr_dict=sorted(arr_dict.items(),key=operator.itemgetter(0)) #0은 키, 1은 값 기준으로 정렬
for str,cnt in arr_dict:
    print('%s %.4f' %(str,cnt/count*100))
