import sys
sys.stdin = open('1976_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    h1 = (list(map(int, input().split())))
    hour = 0
    minute = 0
    hour = h1[0] + h1[2]
    minute = h1[1] + h1[3]
    if hour > 12:
        hour -= 12
    if minute > 59:
        hour += 1
        minute -= 60
    print(f"#{test_case} {hour} {minute}")

    