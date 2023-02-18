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
    if count[A[0]] == 2:
        out.append(A[0])
        out.append(result[A[0]])
for i in count.keys():
    if count[i] == 1:
        if i == 1 or i == 2:
            x = result[i][0]
        elif i == 3 or i == 4:
            y = result[i][0]
y_sub = 0
x_sub = 0
if out[0] >= 3:
    y_sub = out[1][1]
    x_sub = out[3][0]
else:
    y_sub = out[3][0]
    x_sub = out[1][1]

total = x*y
sub = y_sub*x_sub
print((total-sub)*k)





