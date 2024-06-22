from collections import deque

N = int(input())

d = deque()
for _ in range(N):
    cmd = input()
    if cmd.startswith('push_front'):
        _, a = cmd.split()
        a = int(a)
        d.append(a)
    elif cmd.startswith('push_back'):
        _, a = cmd.split()
        a = int(a)
        d.appendleft(a)
    elif cmd.startswith('pop_front'):
        print(d.pop())
    elif cmd.startswith('pop_back'):
        print(d.popleft())
    elif cmd.startswith('size'):
        print(len(d))
    elif cmd.startswith('empty'):
        print(1 if len(d) == 0 else 0)
    elif cmd.startswith('front'):
        print(d[-1])
    elif cmd.startswith('back'):
        print(d[0])