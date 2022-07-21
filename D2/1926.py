n = int(input())

clap = ['3', '6', '9']

for i in range(1, n + 1):
    num = str(i)
    count = 0
    for j in num:
        if j in clap:
            count += 1
    
    if count > 0:
        print(count * '-', end = '')
    else:
        print(i, end = '')