import sys
sys.stdin = open("2029_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"#{test_case} {A // B} {A % B}")