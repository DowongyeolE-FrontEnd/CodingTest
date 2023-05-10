import sys

time = int(input())

input = sys.stdin.readline
#input 보다는 sys.stdin.readline 써야 하는 이유 정리하기

stack = []
top = -1
for i in range(time):
    put = input().split()
    if put[0] == 'push':
        stack.append(int(put[1]))
        top += 1
    elif put[0] == 'pop':
        if top != -1:
            print(stack.pop())
            top += -1
        else:
            print(-1)
    elif put[0] == 'top':
        if top != -1:
            print(stack[top])
        else:
            print(-1)
    elif put[0] == 'size':
        print(top+1)
    elif put[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)