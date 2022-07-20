import sys

sys.stdin = open('1284_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    b_company = 0
    a_company = w * p
    if r > w:
        b_company += q
    else:
        b_company += q + (w - r) * s
    choice = min(a_company, b_company)
    print(f"#{test_case} {choice}")
 