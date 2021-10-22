#단어공부
import sys
input=sys.stdin.readline
word=input().strip()

word_list=[]
word_dict={}
#대문자로 바꾸기
for i in range(0,len(word)):
    word_list.append(word[i].upper())

#갯수세기
for i in word_list:
    if i not in word_dict:
        word_dict[i]=1
    else:
        word_dict[i]+=1

#값 순대로 정렬
word_sort= sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

if len(word_sort)==1:
    print(word_sort[0][0])
elif word_sort[0][1]==word_sort[1][1]:
    print('?')
else:
    print(word_sort[0][0])

