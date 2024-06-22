string = input()

stack = []
for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
    else:
        if len(stack) == 0 or stack[-1] != '(':
            print('No')
            break
        else:
            stack.pop()

if len(stack) == 0:
    print('Yes')