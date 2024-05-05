N, L = list(map(int, input().split()))
nums = list(map(int, input().split()))

answer = 0
for H in range(0, 101):
    valid = 0
    subvalid = 0
    for num in nums:
        if num >= H:
            valid += 1
        elif num+1 >= H:
            subvalid += 1
    
    if valid+min(L, subvalid) >= H:
        answer = max(answer, H)

print(answer)