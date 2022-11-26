T = int(input())
for test_case in range(1,T+1):
    n, k = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(n)]
    ans = 0 #정답은 가로, 세로 모두 누적되어야 하므로 밖에서 변수선언
    
    for i in range(n): #가로부터 확인하기
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == n-1: #0인곳을 만났건, 벽에 다았을때
                if cnt == k:
                    ans += 1
                if puzzle[i][j] == 0:
                    cnt =0

    for j in range(n): #세로 확인하기
        cnt = 0
        for i in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or i == n-1: #0인곳을 만났건, 벽에 다았을때
                if cnt == k:
                    ans += 1
                if puzzle[i][j] == 0 :
                    cnt =0    
                    
                    
    print("#{} {}". format(test_case, ans))