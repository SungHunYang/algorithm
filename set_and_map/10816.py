import sys


N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))
hash = {}

for i in N_list:
    if i not in hash.keys():
        hash[i] = 1
    else:
        hash[i] += 1

for i in M_list:
    if i not in hash.keys():
        print('0',end=' ')
    else:
        print(f"{hash[i]}",end=' ')