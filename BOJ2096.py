# 2020/11/30
import sys
N = int(sys.stdin.readline())
mindp = [[0 for i in range(3)] for i in range(2)]
maxdp = [[0 for i in range(3)] for i in range(2)]

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    
    maxdp[1][0] = max(maxdp[0][0], maxdp[0][1]) + arr[0]
    maxdp[1][1] = max(maxdp[0][0], maxdp[0][1], maxdp[0][2]) + arr[1]
    maxdp[1][2] = max(maxdp[0][1], maxdp[0][2]) + arr[2]
    
    mindp[1][0] = min(mindp[0][0], mindp[0][1]) + arr[0]
    mindp[1][1] = min(mindp[0][0], mindp[0][1], mindp[0][2]) + arr[1]
    mindp[1][2] = min(mindp[0][1], mindp[0][2]) + arr[2]
    mindp.pop(0)
    maxdp.pop(0)
    mindp.append([0 for i in range(3)])
    maxdp.append([0 for i in range(3)])
print(max(maxdp[0]), min(mindp[0]))