num = int(input())
score = list(map(int,input().split()))

sum = 0
max = 0
for i in score:
    if i > max:
        max = i
for i in score:
    sum += (i/max)*100


print(sum/num)
