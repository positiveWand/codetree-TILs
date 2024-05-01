n = int(input())
hint = {}
for _ in range(n):
    key, count1, count2 = input().split()
    hint[key] = (int(count1), int(count2))

# print(hint)
answer = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
                
            test = 100*i+10*j+k
            test = str(test)
            
            valid = 0
            for num, count in hint.items():
                test_count = [0,0]

                if test[0] == num[0]:
                    test_count[0] += 1
                elif test[0] == num[1] or test[0] == num[2]:
                    test_count[1] += 1
                
                if test[1] == num[1]:
                    test_count[0] += 1
                elif test[1] == num[0] or test[1] == num[2]:
                    test_count[1] += 1
                
                if test[2] == num[2]:
                    test_count[0] += 1
                elif test[2] == num[0] or test[2] == num[1]:
                    test_count[1] += 1
                
                if test_count[0]==count[0] and test_count[1]==count[1]:
                    valid += 1
            
            if valid == n:
                answer += 1
                

print(answer)