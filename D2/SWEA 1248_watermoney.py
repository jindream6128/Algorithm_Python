T = int(input())

for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    ansA, ansB =0,0
    ansA = P*W

    if W <= R:
        ansB = Q
    else:
        ansB = Q + S*(W-R)

    if ansA < ansB:
        print(f'#{test_case} {ansA}')
    else:
        print(f'#{test_case} {ansB}')