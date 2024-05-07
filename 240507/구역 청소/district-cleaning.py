a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

overlap = 0
if c < b < d and a < c < b:
    overlap = b-c
elif c < a < d and a < d < b:
    overlap = d-a
elif c < a < b < d:
    overlap = b-a
elif a < c < d < b:
    overlap = d-c


print(abs(b-a)+abs(d-c)-overlap)