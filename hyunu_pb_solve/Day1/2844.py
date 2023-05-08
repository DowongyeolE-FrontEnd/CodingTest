a = list(map(int, input().split()))

hour = a[0] #시간
mini = a[1] #분

if mini - 45 < 0:
    if hour - 1 < 0:
        print(23, (60 + mini-45))
    else:
        print(hour-1, (60 + mini-45) )
else:
    print(hour, mini-45)