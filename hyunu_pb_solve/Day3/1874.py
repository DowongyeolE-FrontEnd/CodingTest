import sys

input = sys.stdin.readline
#이 문제도 이게 크게 작용하네

list = [i for i in range(1,10)]

stack = []

time = int(input())

idx = 0
top = -1
for j in range(time):
    num = int(input())
    while(1):
        if stack[top] == num:
            stack.pop()
            top = -1
            print('-')
            break;
        if list[idx] <= num:
            stack.append(list[idx])
            idx += 1
            top += 1
            print('+')
       
