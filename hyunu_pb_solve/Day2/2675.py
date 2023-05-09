time = int(input())

for i in range(time):
    result = ''
    put = input().split()
    word = put[1]
    cnt = int(put[0])
    for i in range(len(word)):
        for j in range(cnt):
            result += word[i]
    print(result)
