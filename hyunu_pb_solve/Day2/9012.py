con = int(input()) #입력 횟수

for i in range(con):
    top = -1
    stack = []
    ps = input()
    for i in range(len(ps)):
        
        #0이면 그냥 넘어가기 
        if top == -1:
            stack.append(ps[i])
            top += 1
        else:
            if stack[top] == "(" and ps[i] == ")":
                stack.pop()
                top -= 1
            else:
                stack.append(ps[i])
                top += 1
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

