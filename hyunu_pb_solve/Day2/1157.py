word = input()

vis = [0 for i in range(26)]

# 소문자는 65 대문자는 97 / 97-26 = 71

word = word.upper()
for i in word:
    vis[ord(i)-65] += 1

max = 0
idx = 0

for i in range(len(vis)):
    if vis[i] > max:
        max = vis[i]
        idx = i

count = 0

for i in vis:
    if max == i:
        count += 1

if count == 1:
    print(chr(idx+65))
else:
    print('?')

