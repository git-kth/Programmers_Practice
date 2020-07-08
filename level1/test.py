import sys
s = sum([i for i in range(int(input()) + 1)])
s -= sum(map(int,sys.stdin.readline().split()))
print(s)
