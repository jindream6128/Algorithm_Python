# file input
import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N =int(input()) #100 고정
    arr = [list(map(int,input().split())) for _ in range(N)] #100*100 배열 완성
    cnt = 0
    # 1번이 arr[i][j]에서 i가 커질때마다 한칸씩 내려가다가 2번을 만나면 cnt += 1그러고 난뒤에 다음 j로 간다
    for j in range(0, N):
        for i in range(0,N-1):
            if arr[i][j] == 1:
                if arr [i+1][j] == 2:
                    cnt += 1
    print(f'{cnt}')