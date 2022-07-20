import sys
sys.stdin = open('2056_input.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    # print(f"{test_case + 1}", end =' ')
    dates = str(input())
    year, month, day = int(dates[0:4]), int(dates[4:6]), int(dates[6:8])

    if month == 2:
        if day < 1 or day > 28:
            print(-1)
            continue
    
    if month < 1 or month > 12:
        print(-1)
        continue
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            print(-1)
            continue
    
    if month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            print(-1)
            continue
    
    print(f"{year}/{month}/{day}")