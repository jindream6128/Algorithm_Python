T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    dis = list(map(int, input().split())) # 거리를 입력받는다
    dis_r = [] #절댓값이 저장될 리스트 생성

    for i in range(0, N):
        dis_r.append(abs(dis[i])) #절댓값을 dis_r 리스트에 저장

    print(f'#{test_case} {min(dis_r)} {dis_r.count(min(dis_r))}') #절댓값중 min이 가장 가까운값, 동일한 값을 몇개 가지는지 count
