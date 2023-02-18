import sys

N = int(sys.stdin.readline())
result = list(map(int,sys.stdin.readline().split()))

num = 2
while True:
    check = 0
    for i in result:
        if num%i != 0:
            num+=1
            check = 1
            break
        if num//i not in result:
            num += 1
            check = 1
            break

    if check:
        continue

    if num in result:
        num+=1
        continue

    break

print(num)