import sys

input = sys.stdin.readline

put = input().split()

N = int(put[0])
K = int(put[1])

queue = [i for i in range(1,N+1)]

front = 0
rear = 0
idx = K-1

result = []

for i in range(N):
    # print(idx)
    # print("queue",queue)
    # print("result",result)
    if i == N-1:
        result.append(queue[0])
        break;
    if idx < len(queue):
        result.append(queue.pop(idx))
        idx += (K-1)
    elif idx >= len(queue):
        idx = idx % len(queue)
        result.append(queue.pop(idx))
        idx += (K-1)

output = ', '.join(str(s) for s in result)
print("<"+output+">")