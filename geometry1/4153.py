import sys

result = []
while True:

    A = list(map(int,sys.stdin.readline().split()))
    if A[0] == 0 and A[1] == 0 and A[2] == 0:
        break
    else:
        result.append(A)

for i in range(len(result)):
    big = max(result[i])
    result[i].remove(big)
    A,B = result[i][0]**2,result[i][1]**2
    if big**2 == (A + B):
        print('right')
    else:
        print('wrong')
