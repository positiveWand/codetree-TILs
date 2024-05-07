n,m,p = tuple(map(int, input().split()))
messages = []
for _ in range(m):
    programmer, left = input().split()
    messages.append((programmer, int(left)))

suspect = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:n])
for i, message in enumerate(messages):
    programmer, left = message
    if i < p-1:
        continue

    suspect.discard(programmer)
    if left == 0:
        suspect -= set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

print(' '.join(sorted(list(suspect))))