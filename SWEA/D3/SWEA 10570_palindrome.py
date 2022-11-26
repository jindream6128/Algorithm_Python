import sys
sys.stdin = open("input.txt", "r")
#여기서 중요한건 type잘 생각해보자 루트(제곱근) 값이 무조건 정수가 아니기 때문
T = int(input())
for tc in range(1,T+1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A,B+1):
        num = i**(1/2)
        i =str(i)
        if num == int(num): #정수일때
            num = str(int(num))
            if num==num[::-1] and i==i[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')