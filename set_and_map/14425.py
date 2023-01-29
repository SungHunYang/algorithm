import sys

N, M = map(int,sys.stdin.readline().split())

N_list = []
M_list = []

for i in range(N):
    N_list.append(sys.stdin.readline().strip())
for i in range(M):
    M_list.append(sys.stdin.readline().strip())

A = set(N_list)

cnt = 0
for i in M_list:
    if i in A:
        cnt += 1

print(cnt)
