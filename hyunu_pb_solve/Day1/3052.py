num = []
result = [0 for i in range(42)]

for i in range(10):
    num.append(int(input())%42)
    result[num[i]] += 1

count=0
for i in result:
    if i !=0:
        count += 1
print(count)