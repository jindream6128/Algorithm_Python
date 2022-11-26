T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split()) #N,M 입력
    arr = [list(map (int,input().split())) for a in range(N)] # N크기의 2차원 배열 생성
    ans = 0 #최대값을 찾기위한 변수
    
    for si in range(0, N-M+1): #i의 시작좌표
        for sj in range(0,N-M+1): #j의 시작좌표
            cnt = 0 #파리 갯수 더할 변수선언
            for i in range(si,si+M): #M크기의 파리채 i좌표 si 즉 시작좌표에서 M의 크기만큼
                for j in range(sj, sj+M): #sj 시작좌표에서 M의 크기만큼
                    cnt += arr[i][j] #파리의 갯수 세기
    
            if ans<cnt: #최대값 구하기
                ans=cnt
                
    print("#{} {}".format(test_case,ans))