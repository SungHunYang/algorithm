import sys

k = int(sys.stdin.readline())
result = {1:[],2:[],3:[],4:[]}
x = 0
y = 0
total = 0
count = {1:0,2:0,3:0,4:0}
out=[]
for i in range(6):
    A = list(map(int,sys.stdin.readline().split()))
    count[A[0]] += 1
    result[A[0]].append(A[1])