con = int(input()) #입력 횟수

group_word = 0

for i in range(con):
    stack = [0 for i in range(26)]
    word = input()
    for i in range(len(word)):
        if i == 0:
            #알파벳이 아스키코드로 a 부터 97
            #ord, chr 를 해주면 아스키코드에서 문자로 왔다갔다 할 수 있음. 
            stack[ord(word[i])-97] += 1
        else:
            if word[i-1] == word[i]:
                continue;
            else:
                stack[ord(word[i])-97] += 1
    count = 0
    for i in stack:
        if i > 1:
            count += 1
    if count == 0:
        group_word += 1

print(group_word)
