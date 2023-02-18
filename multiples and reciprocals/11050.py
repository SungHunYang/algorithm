import sys
r = int(sys.stdin.readline())
quiz = []
for i in range(r):
    quiz.append(list(map(int,sys.stdin.readline().split())))

for i in quiz:
    K,N = i
    sum = 1
    div = 1
    if K == 0:
        print(1)
    else:
        for i in range(K):
            sum = sum*(N-i)
            div = div*(i+1)
        print(sum//div)