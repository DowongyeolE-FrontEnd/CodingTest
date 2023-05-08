a = int(input())

min = 1000001
max = -1000001

data = list(map(int,input().split()))

for i in range(a):
    if data[i] > max:
        max = data[i]
    if data[i] < min:
        min = data[i]

print(min,max)

#문제조건 잘읽기, max, 음수도 들어갈 수 있는데 0으로 잡아서 틀림