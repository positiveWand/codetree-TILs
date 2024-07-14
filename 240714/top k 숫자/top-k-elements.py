n, k = list(map(int, input().split()))

nums = set(map(int, input().split()))
nums = list(nums)

nums.sort(reverse=True)

print(' '.join(list(map(str, nums[:k]))))