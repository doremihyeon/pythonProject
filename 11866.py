from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))

arr = []
while len(queue) != 0:
    # while not queue(큐가 비지 않았을 때)로 써서 만들 수 도있음
    for _ in range(K-1):
        queue.append(queue.popleft())
    arr.append(str(queue.popleft()))
print('<'+', '.join(arr)+'>')