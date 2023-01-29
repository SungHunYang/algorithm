import sys

N, M = map(int,sys.stdin.readline().split())
N_list = set()
M_list = set()
for i in range(N):
    N_list.add(sys.stdin.readline().strip())

for i in range(M):
    M_list.add(sys.stdin.readline().strip())

A = list(N_list.intersection(M_list))
A.sort()

print(len(A))
for i in A:
    print(i)