S = input()
answer = set()
#ababc a b a b c ab ba ab bc aba bab abc abab babc ababc
for i in range(len(S)):
    for j in range(i,len(S)):
        temp = S[i:j+1]
        answer.add(temp)

print(len(answer))
