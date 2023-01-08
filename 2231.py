import sys

def cal(num):

    sum = num
    while True:
        rest = num % 10
        sum += rest
        num //= 10

        if num == 0:
            break

    return sum

N = int(sys.stdin.readline())

num = 0
ans = []
while True:

    result = cal(num)

    if result == N :
        ans.append(num)

    num += 1

    if num >= N:
        break

if len(ans) == 0:
    print(0)
else :
    print(ans[0])

