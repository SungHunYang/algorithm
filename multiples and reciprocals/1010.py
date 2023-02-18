import sys

N,K = map(int,input().split())

sum = 1
div = 1
if K == 0:
    print(1)
else:
    for i in range(K):
        sum = sum*(N-i)
        div = div*(i+1)
    print((sum//div))