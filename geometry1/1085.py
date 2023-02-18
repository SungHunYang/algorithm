import sys

x,y,w,h = map(int,sys.stdin.readline().split())

dit = 0

dit = min(x,y,(w-x),(w-y))
