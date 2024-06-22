from collections import deque

N, K = list(map(int, input().split()))

queue = deque()
answer = []
for i in range(1, N+1):
    queue.append(i)

while len(queue) > 0:
    for _ in range(K-1):
        queue.append(queue.popleft())
    
    answer.append(queue.popleft())

print(' '.join(list(map(str, answer))))