import sys
sys.stdin = open("2071_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(T):
    num = list(map(int, input().split()))
    result = sum(n for n in num)
    print(f"#{i+1} {round(result/10)}")