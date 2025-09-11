import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, -x)

    elif x == 0:
        if heap:
            max = -heapq.heappop(heap)
            print(max)
        else:
            print(0)