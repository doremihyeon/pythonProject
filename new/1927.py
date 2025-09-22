import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, x)

    if x == 0:
        if heap:
            print(heap[0])
            heapq.heappop(heap)

        else:
            print(0)