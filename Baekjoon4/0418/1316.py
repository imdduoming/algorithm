#구현알고리즘
#그룹단어체커
import sys
input=sys.stdin.readline
N=int(input())
words=[]


for i in range(N):
    word=input().strip()
    words.append(word)

def solve(word):
    dict={}
    group=1 #초기화는 그룹단어로
    for i in range(0,len(word)):
        if word[i] not in dict:
            dict[word[i]]=i
        else:
            if i-dict[word[i]]!=1:
                group=0
                break
            dict[word[i]]=i


    if group==0:
        return False
    else:
        return True
count=0
for i in words:
    if solve(i):
        count+=1


print(count)