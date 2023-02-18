import sys


quiz = []
result = []
while True:
    a,b = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    quiz.append((a,b))

for a,b in quiz:
    if a > b:
        if a%b == 0:
            result.append('multiple')
        else:
            result.append('neither')

    else:
        if b%a == 0:
            result.append('factor')
        else:
            result.append('neither')

for i in result:
    print(i)