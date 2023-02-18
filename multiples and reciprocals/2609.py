import sys

N = int(sys.stdin.readline().split())
a,b = map(int,sys.stdin.readline().split())

a_sub = set()
b_sub = set()
inter = set()
union = set()

num = 1
while True:

    if a%num == 0 :
        a_sub.add(num)
        a_sub.add(a//num)

    if b%num == 0 :
        b_sub.add(num)
        b_sub.add(b//num)

    if num > min(a,b):
        break
    num += 1

inter = a_sub.intersection(b_sub)
print(max(inter))
print(a*b//max(inter))
