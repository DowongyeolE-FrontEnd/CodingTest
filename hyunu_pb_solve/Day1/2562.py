a = []

max = 0 
pc = 0

for i in range(9):
    a.append(int(input()))
    if a[i] > max:
        max = a[i]
        pc = i

print(max)
print(pc+1)