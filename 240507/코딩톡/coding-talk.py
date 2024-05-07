n,m,p = tuple(map(int, input().split()))
messages = []
for _ in range(m):
    programmer, left = input().split()
    messages.append((programmer, int(left)))

suspects = [None for _ in range(m)]

for i in range(p):
    new_suspect = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:n])
    for j, message in enumerate(messages[i:]):
        programmer, left = message

        new_suspect.discard(programmer)
        if left == 0:
            new_suspect -= set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # print(new_suspect)
    if i != 0:
        if messages[i][1] == messages[i-1][1]:
            new_suspect = set(suspects[i-1])
        
    suspects[i] = new_suspect

# print(suspects)

print(' '.join(sorted(list(suspects[p-1]))))