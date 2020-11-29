# 2020/11/30
import sys
import heapq
N = int(input())
heap = list(map(int, sys.stdin.readline().split()))
for i in range(1, N):
    temp = map(int, sys.stdin.readline().split())
    for j in temp:
        heapq.heappush(heap, j)
    for j in range(N):
        heapq.heappop(heap)
print(heap[0])