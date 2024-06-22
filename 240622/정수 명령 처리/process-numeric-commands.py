N = int(input())

stack = []

for _ in range(N):
    cmd = input()
    if cmd.startswith('push'):
        _, a = cmd.split()
        a = int(a)
        stack.append(a)
    elif cmd.startswith('pop'):
        print(stack.pop())
    elif cmd.startswith('size'):
        print(len(stack))
    elif cmd.startswith('empty'):
        print(1 if len(stack) == 0 else 0)
    elif cmd.startswith('top'):
        print(stack[-1])