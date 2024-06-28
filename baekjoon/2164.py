from collections import deque

#입력을 다 큐에 저장한다. (큐는 1 2 3 4 가 된 상태)
N = int(input())
queue = deque(range(1, N + 1))

#큐에 내용물이 하나가 남을 때까지 아래 과정을 반복한다.
while len(queue) > 1:
    #큐에서 카드 한 장을 꺼내서 버린다.
    discarded_card = queue.popleft()

    # 큐에서 카드 한 장을 꺼내서 맨 뒤에 추가한다.
    moved_card = queue.popleft()
    queue.append(moved_card)

remaining_card = queue.popleft()
print(remaining_card)





