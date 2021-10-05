import sys
import collections
input = sys.stdin.readline #빠른 입력
def search(arr,start,end):
    root=arr[start]
    for i in range(start+1,end+1):

        if arr[i]>root:
            return i


def postorder(arr,start,end):
    if start>=end:
        return
    upperindex=search(arr,start,end)
    #print(upperindex)

    postorder(arr,start+1,upperindex-1)

    postorder(arr,upperindex,end)
    print(arr[start])




arr=[]
while True:
    try:
        num=int(input())
        arr.append(num)
    except:
        break
print('arr:',arr)
postorder(arr,0,len(arr)-1)