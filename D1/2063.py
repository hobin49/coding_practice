import sys
sys.stdin = open('2063_input.txt', 'r')

N = int(input())
num = list(map(int, input().split()))
num.sort()
middle = (N-1) // 2 # 가운데 값 구할면 
print(f"{num[middle]}")