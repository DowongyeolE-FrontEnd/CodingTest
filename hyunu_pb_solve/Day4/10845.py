import sys

time = int(input())

input = sys.stdin.readline
#input 보다는 sys.stdin.readline 써야 하는 이유 정리하기

queue = []
for i in range(time):
    put = input().split()
    if put[0] == 'push':
        queue.append(int(put[1]))
    elif put[0] == 'pop':
        if queue : print(queue.pop(0))
        else:
            print(-1)
    elif put[0] == 'front':
        if len(queue) == 0: print(-1)
        else:
            print(queue[0])
    elif put[0] == 'back':
        if len(queue) == 0: print(-1)
        else:
            print(queue[-1])
    elif put[0] == 'size':
        print(len(queue))
    elif put[0] == 'empty':
        if len(queue) == 0: print(1)
        else:
            print(0)