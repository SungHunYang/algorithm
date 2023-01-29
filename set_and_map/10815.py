import sys


N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))

N_list.sort()


def binarysearch(k,N_list):
    start = 0
    last = N - 1
    while start <= last:

        mid = ( start + last ) // 2

        if k == N_list[mid]:
            return 1
        elif k < N_list[mid]:
            last = mid - 1
        elif k > N_list[mid]:
            start = mid + 1

    return 0

for i in M_list:
    print(binarysearch(i,N_list),end=' ')




