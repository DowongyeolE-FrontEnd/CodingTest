import sys
import time
startTime = time.time()

count = int(input())

input = sys.stdin.readline
#input 보다는 sys.stdin.readline 써야 하는 이유 정리하기

cnt = 1
if count == 1:
    print(1)
else:
    if count % 2 == 0:
        cnt = 0
    queue = [i for i in range(2, count+1, 2)]
    while(1):
        if len(queue)==1:
            break;
        if cnt == 0:
            queue.pop(0)
            cnt = 1
        else:
            queue.append(queue.pop(0))
            cnt = 0
    print(queue[0])

print(time.time() - startTime)