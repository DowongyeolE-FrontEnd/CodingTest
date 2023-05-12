import sys
from collections import deque

time = int(input())

input = sys.stdin.readline
#input 보다는 sys.stdin.readline 써야 하는 이유 정리하기

queue = deque(range(2, time+1, 2))

cnt = 1
if time == 1:
    print(1)
else:
    if time % 2==0:
        cnt = 0
    while(1):
        if len(queue) == 1:
            break;
        if cnt == 0:
            queue.popleft()
            cnt = 1
        else:
            queue.append(queue.popleft())
            cnt = 0
    print(queue[0])
