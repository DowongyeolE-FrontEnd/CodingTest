a = input()

count = 0

if int(a)<10:
    a = '0'+a

x = a[0]
y = a[1]

while(1):
    temp = str((int(x)+int(y))%10)   
    count += 1 
    if y+temp == a:
            break;
    else:
         x = y
         y = temp
print(count)