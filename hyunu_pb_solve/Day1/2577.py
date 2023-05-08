a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)

used_num = [0 for i in range(10)]

for i in range(len(result)):
    used_num[int(result[i])] += 1

for i in used_num:
    print(i)