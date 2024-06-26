n,k = list(map(int, input().split()))
nums = list(map(int, input().split()))

answer = float('inf')
for idx, max_num in enumerate(nums):
    if max_num < nums[0] or max_num < nums[len(nums)-1]:
        continue

    idx_arr = [0]
    for i, num in enumerate(nums):
        if i == 0 or i == len(nums)-1:
            continue
        if max_num >= num:
            idx_arr.append(i)
    idx_arr.append(len(nums)-1)

    fail = False
    for i in range(1, len(idx_arr)):
        distance = idx_arr[i]-idx_arr[i-1]
        if distance > k:
            fail = True
            break
    if fail:
        continue
    
    answer = min(max_num, answer)

print(answer)