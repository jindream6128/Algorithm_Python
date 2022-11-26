T = int(input())

for test_case in range(1, T+1):
    a,b,c,d,e =0,0,0,0,0 # 2 3 5 7 11 소수의 지수 a b c d e
    num = int(input())
        # 소인수 부해를 하는 과정을 잘 찾아야함
        # 작은 수부터 나머지가 0이도록 계속 나눈다.
        # 나눈 몫을 다시 나머지가 0 이 되도록 나눈다.
    while num % 2 == 0:
        a += 1
        num = num // 2
    while num % 3 == 0:
        b += 1
        num = num // 3
    while num % 5 == 0:
        c += 1
        num = num // 5
    while num % 7 == 0:
        d += 1
        num = num // 7
    while num % 11 == 0:
        e += 1
        num = num // 11

    print(f'#{test_case} {a} {b} {c} {d} {e}')
