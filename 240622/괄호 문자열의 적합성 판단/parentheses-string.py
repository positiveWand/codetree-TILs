string = input()

stack = []
for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
    else:
        if len(stack) == 0 or string[i] == ')':
            print('No')
            break
        stack.pop()

if len(stack) == 0:
    print('Yes')