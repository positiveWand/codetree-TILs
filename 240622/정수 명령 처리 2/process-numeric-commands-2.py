from collections import deque

N = int(input())

queue = deque()
for _ in range(N):
    cmd = input()
    if cmd.startswith('push'):
        _, a = cmd.split()
        a = int(a)
        queue.append(a)
    elif cmd.startswith('pop'):
        print(queue.popleft())
    elif cmd.startswith('size'):
        print(len(queue))
    elif cmd.startswith('empty'):
        print(1 if len(queue) == 0 else 0)
    elif cmd.startswith('front'):
        print(queue[0])