word = input()

# ABC,DEF,GHI,JKL,MNO,PQRS,TUV,WXYZ
list =[3,3,3,3,3,4,3,4]

# 첫칸 돌리는데 3


count = 0
for i in word:
    init = 3 # 기본 소요 시간
    sum = 0
    for num in list:
        sum += num
        if (ord(i)-65) < sum:
            count += init
            break;
        else:
            init += 1
print(count)