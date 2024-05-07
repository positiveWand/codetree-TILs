a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

if b <= c or d <= a:
    overlap = 0
else:
    if c < b < d:
        overlap = b-c - max(0, c-a)
    elif c < a < d:
        overlap = d-a - max(0, d-b)


print(abs(b-a)+abs(d-c)-overlap)