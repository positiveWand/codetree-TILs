abilities = list(map(int, input().split()))

answer = float('inf')

for i in range(len(abilities)):
    for j in range(i+1, len(abilities)):
        for k in range(len(abilities)):
            for l in range(k+1, len(abilities)):
                if i == k or j == l or i == l or j == k:
                    continue
                
                # count += 1
                first = abilities[i]+abilities[j]
                second = abilities[k]+abilities[l]
                third = sum(abilities)-first-second

                if max(first, second, third) - min(first, second, third) < answer and first != second != third:
                    
                    answer = max(first, second, third) - min(first, second, third)
                    # print(first, second, third)
# print(count)
if answer == float('inf'):
    print(-1)
else:
    print(answer)