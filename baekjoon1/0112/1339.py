import sys
N=int(sys.stdin.readline())
word_arr=[]
for i in range(0,N):
    word_arr.append(input())



alphabet={}


sum=0

for word in word_arr:
    count=0
    for alpha in word:
        if alpha not in alphabet: #알파벳의 점수가 책정되지않은경우
            alphabet[alpha] = 10**(len(word)-1-count)

        else:
            alphabet[alpha] += 10 ** (len(word) - 1 - count)
        count+=1
alphabet=sorted(alphabet.items(),key=lambda x:x[1],reverse=True)
score=9

for (key,value) in alphabet:

    sum=sum+score*value
    score-=1
print(sum)