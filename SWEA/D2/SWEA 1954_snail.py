T = int(input())
di = [0,1,0,-1] #i와 j의 방향 전환
dj = [1,0,-1,0]

for test_case in range(1,T+1):
    N=int(input())
    
    i,j,cnt,dr = 0,0,1,0 # 초기화
    arr = [[0]*N for _ in range(N)] # 초기값이 0 인 배열 만들기 
    arr[i][j] = cnt 
    cnt += 1
    
    while cnt<= N*N: #cnt의 값이 N*N보다 작은 범위
        ni = i + di[dr]#다음 i좌표
        nj = j + dj[dr]#다음 j좌표
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0: #범위내, 해당 범위의 값이 초기값 0 이어야 한다.
            i, j =ni, nj
            arr[i][j]=cnt
            cnt += 1
        else: #범위 이내가 아니라면 방향을 바꿔야 한다
            dr = (dr+1)%4 #dr 즉 방향은 총4개가 반복된다.
    
    print(f'#{test_case}')
    for lst in arr:
        print(*lst)