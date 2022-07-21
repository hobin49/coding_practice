import sys
sys.stdin = open('1989_input.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    letter = input()
    palindrome = ""
    for char in range(len(letter)-1, -1, -1):
        palindrome += letter[char]
    
    if palindrome == letter:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")