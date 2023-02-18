import sys

N,K = map(int,input().split())

sum = 1
div = 1

if N == 0 or N < K:
    result = str(0)
elif K == 0 or N == K:
    result = str(1)
else:
    if N // 2 < K:
        K = N-K
    for i in range(K):
        sum = sum*(N-i)
        div = div*(i+1)

    result = str(sum//div)

cnt = 0
for i in range(len(result)-1,-1,-1):
    if result[i] == '0':
        cnt+=1
    else:
        break
print(cnt)