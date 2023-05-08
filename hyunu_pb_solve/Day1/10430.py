# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
# a  = input().split()

# A = int(a[0])
# B = int(a[1])
# C = int(a[2])
# 위에 처럼 작성해주는 것 보다 아래처럼 받아주는게 좋음
data = list(map(int, input().split()))

A = data[0]
B = data[1]
C = data[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
