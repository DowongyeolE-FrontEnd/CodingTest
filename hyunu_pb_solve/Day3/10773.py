import sys

input = sys.stdin.readline
#이 문제도 이게 크게 작용하네

time = int(input())

stack = []
top = -1

for i in range(time):
    num = int(input())
    if num == 0:
        if top == -1:
            continue;
        else:
            stack.pop()
    else:
        stack.append(num)
        top += 1

sum = 0

for i in stack:
    sum += i

print(sum)