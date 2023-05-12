import sys

input = sys.stdin.readline
#이 문제도 이게 크게 작용하네


stack = []
result = []

time = int(input())

# list = [i for i in range(1,time)]

idx = 0
top = -1
check = -1

for j in range(time):
    num = int(input())
    if check == -1:
        while(1):
            # print(idx, result, stack)
            if idx < num:
                idx += 1
                stack.append(idx)
                top += 1
                result.append('+')
                continue
                # print('+')
            if stack[top] != num:
                    check += 1
                    break;
            if stack[top] == num:
                    stack.pop()
                    top += -1
                    # print('-')
                    result.append('-')
                    break;
            if idx > time:
                break 
if len(stack) > 0:
    print("NO")
else:
    for i in result:
        print(i)