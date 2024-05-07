n,m,p = tuple(map(int, input().split()))
messages = []
for _ in range(m):
    programmer, left = input().split()
    messages.append((programmer, int(left)))

suspects = [None for _ in range(m)]

for i in range(p):
    new_suspect = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:n])
    for j, message in enumerate(messages):
        programmer, left = message
        if j < p-1:
            continue

        new_suspect.discard(programmer)
        if left == 0:
            new_suspect -= set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if i != 0:
        before_suspect_count = messages[i][1]

        if messages[i][1] == messages[i-1][1]:
            new_suspect = set(suspects[i-1])
        
    suspects[i] = new_suspect

print(' '.join(sorted(list(suspects[p-1]))))