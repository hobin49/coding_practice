import sys
sys.stdin = open('1288_input.txt', 'r')

T = int(input())

for tc in range(T):
    number = input() #문자열 그대로 받아주자 제발 여기서 split쓰지마 왜 쓰니 문제 잘 읽어봐 
    count = 0 #배수 구할때 쓰기
    check = [] # 빈 리스트 만들기
    result = [] # 최종값 담을 리스트

    while len(check) < 10: #개수가 다 되면 끝내
        count += 1 # 배수 구할 때 쓰기 
        increse_n = str(int(number) * count) # number가 string 이니까 count랑 계산하려면 int 변환 해주고 다시 str
        for num in increse_n: #문자 돌아주고
            if num not in check: #없으면 추가해주고
                check.append(num)
    

    result.append(increse_n) #최종값 담아주고

for i in range(T): #이 부분은 문제가 원하는 출력을 하기 위해서 했다. 
    print(f"#{i+1} {result[i]}")



# 다른 풀이

T = int(input())
for test_case in range(1, T + 1):
    #input 가져오기
    N = int(input())
    N1 = N
    #Set에 계속 추가
    numbers = set()
    #while 반복 => Set 길이가 10이 될 때까지
    while len(numbers) < 10:
        #for 반복 : 숫자를 문자로
        for n in str(N):
            numbers.add(n)
        #딱 값이 나오면 끊는다.
        if len(numbers) == 10:
            break

        N += N1
    print(f"#{test_case} {N}")


        
    


        
        


