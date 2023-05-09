word = input() #입력 단어

stack = [-1 for i in range(26)]

for i in range(len(word)):
    if stack[ord(word[i])-97] == -1:
        stack[ord(word[i])-97] = i

# print(stack)
# str = ''.join(arr)
# result = ''.join(stack)
# 숫자는 처리를 더 해줘야 함.
result = ' '.join(str(s) for s in stack)
print(result)