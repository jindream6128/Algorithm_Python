# file input
import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N =int(input()) #100 고정
    arr = [list(map(int,input().split())) for _ in range(N)] #100*100 배열 완성
    cnt = 0
    # 1번이 arr[i][j]에서 i가 커질때마다 한칸씩 내려가다가 2번을 만나면 cnt += 1그러고 난뒤에 다음 j로 간다
    for j in range(0, N):
        state = 0 #상태를 확인하기위에 state = 0을 추가한다
        for i in range(0,N-1):
            if arr[i][j] == 1 and state ==0: #만약 1번(N극이) 있고 상태가 0이라면 1로바꿔준다
                state = 1
            if arr [i+1][j] == 2 and state ==1: #값이 2(s극이고) 상태가 1이라면 위에 N극이 있다는소리라서 cnt를+1해준다
                cnt += 1
                state =0 #한번의 교착상태가 되고 그다음 교착상태를 찾아본다
    print(f'#{test_case} {cnt}')