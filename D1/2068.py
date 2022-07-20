import sys
sys.stdin = open('2068_input.txt', 'r')

T = int(input())

for _ in range(1, T+1):
    A = list(map(int, input().split()))
    max_A = max(A)
    print(f"#{_} {max_A}")
