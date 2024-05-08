n = int(input())
nums = list(map(int, input().split()))

num_count = dict()
for num in nums:
    if num not in num_count:
        num_count[num] = 0    
    num_count[num] += 1

sorted_nums = sorted(list(set(nums)))
if len(sorted_nums) < 2:
    print(-1)
else:
    second_least = sorted_nums[1]

    if num_count[second_least] > 1:
        print(-1)
    else:
        print(nums.index(second_least)+1)