n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

answer = float('inf')
# 구간의 최대값을 가정하여 탐색
for i in range(10001):
    possible = True
    section = 1

    # 최대값을 기준으로 구간 나누기
    subsum = 0
    for j in range(n):
        if nums[j] > i:
            possible = False
            break
        
        if subsum + nums[j] > i:
            subsum = 0
            section += 1
        
        subsum += nums[j]

    # 나눠진 구간들이 성립할 경우에만 갱신
    if possible and section <= m:
        answer = min(answer, i)

print(answer)