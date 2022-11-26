T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    v = 0
    dis = 0
    for i in range(N):
        command = list(map(int,input().split()))

        if command[0] == 1:
            v += command[1]
        elif command[0] == 2:
            if v >command[1]:
                v -= command[1]
            else:
                v = 0
        dis += v
    print(f'#{test_case} {dis}')