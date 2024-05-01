abilities = list(map(int, input().split()))
dev_num = len(abilities)
total_sum = sum(abilities)

answer = float('inf')

for i in range(dev_num):
    for j in range(i+1, dev_num):
        for k in range(j+1, dev_num):
            first_sum = abilities[i]+abilities[j]+abilities[k]
            second_sum = total_sum - first_sum

            answer = min(answer, abs(first_sum-second_sum))

print(answer)