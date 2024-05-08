n = int(input())
nums = list(map(int, input().split()))

positive = []
negative = []
zero = False

for num in nums:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero = True

positive.sort()
negative.sort()

candidate = [0]
if len(positive)>=3:
    candidate.append(positive[-1]*positive[-2]*positive[-3])
if len(negative)>=3:
    candidate.append(negative[-1]*negative[-2]*negative[-3])
if len(positive)>=1 and len(negative)>=2:
    candidate.append(positive[-1]*negative[0]*negative[1])
if len(negative)>=1 and len(positive)>=2:
    candidate.append(negative[-1]*positive[0]*positive[1])


print(max(candidate))