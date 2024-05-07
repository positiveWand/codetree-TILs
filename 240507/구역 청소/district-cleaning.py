a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

if b <= c or d <= a:
    overlap = 0
else:
    if c < b < d and a < c < b:
        overlap = b-c
    elif c < a < d and a < d < b:
        overlap = d-a
    elif c < a < b < d:
        overlap = b-a
    elif a < c < d < b:
        overlap = c-d


print(abs(b-a)+abs(d-c)-overlap)