X, Y = tuple(map(int, input().split()))

answer = 0
for test_num in range(X,Y+1):
    digits = list(map(int, list(str(test_num))))

    fail = False

    # 일일이 포인터로 함
    # 그냥 수열을 뒤집어서 비교했으면 훨씬 간편
    for i in range(len(digits) // 2):
        if digits[i] != digits[len(digits)-1-i]:
            fail = True
    
    if not fail:
        answer += 1
    
print(answer)