import sys

N, M = map(int,sys.stdin.readline().split())
N_list = set(map(int,sys.stdin.readline().split()))
M_list = set(map(int,sys.stdin.readline().split()))

A = N_list.difference(M_list)
B = M_list.difference(N_list)

print(len(A)+len(B))
