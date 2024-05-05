N = int(input())
heights = [int(input()) for _ in range(N)]

answer = float('inf')
# 최소 높이를 가정
for min_height in range(1, max(heights)+1):
    cost = 0

    for h in heights:
        if h < min_height:
            cost += abs(min_height-h)**2
        elif min_height+17 < h:
            cost += abs(min_height+17-h)**2

    answer = min(cost, answer)

print(answer)