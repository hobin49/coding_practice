import sys

sys.stdin = open('2072_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    A = list(map(int, input().split()))
    result = 0
    for i in A:
        if i % 2 == 1:
            result += i

    print(f"#{test_case} {result}")
