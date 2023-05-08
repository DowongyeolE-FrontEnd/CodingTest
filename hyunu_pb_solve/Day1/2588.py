a = input()
b = input()

# for i in range(2,-1,-1):
#     print(int(a)*int(b[i]))
# 위에 처럼 하면 오히려 써줘야 되는 게 많아지는 듯

for i in reversed(range(3)):
    print(int(a)*int(b[i]))

print(int(a)*int(b))