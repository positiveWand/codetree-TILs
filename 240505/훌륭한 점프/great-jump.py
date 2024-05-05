n,k = list(map(int, input().split()))
nums = list(map(int, input().split()))

answer = float('inf')
for max_num in nums:
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