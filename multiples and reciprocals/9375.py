import sys

N = int(sys.stdin.readline())
result = []
for i in range(N):
    R = int(sys.stdin.readline())
    e = dict()
    for i in range(R):
        a,b = sys.stdin.readline().split()
        if b in e.keys():
            e[b].append(a)
        else:
            e[b] = [a]
    result.append(e)


for dic in result:
    sum = 1
    for i in dic.keys():
        sum = sum*( len(dic[i])+1 )

    print(sum-1)
