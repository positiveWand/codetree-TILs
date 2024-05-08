A, B, x, y = list(map(int, input().split()))

print(min(
    abs(A-B),
    abs(A-x)+abs(B-y),
    abs(A-y)+abs(B-x)
))