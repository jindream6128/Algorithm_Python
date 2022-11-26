import sys
sys.stdin = open("input.txt", "r")

dct = {} #값으로 좌표 호출하는 딕셔너리
r_dct = {} #좌표로 값 호출하는 딕셔너리
x, y = 1, 1 #시작 좌표
for n in range(1, 500000): #n은 좌표의 번호
    dct[n] = (x, y)
    r_dct[(x, y)] = n
    x, y = x+1, y-1 #좌표의 변화
    if y <1:
        x, y = 1, x #만약 y가 0으로 가면 다시 위로

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())

    px, py = dct[p] #p값의 x, y좌표 저장
    qx, qy = dct[q] #q값의 x, y좌표 저장

    result = r_dct[(px+qx, py+qy)] #변경된 좌표로 값 호출
    print(f'#{tc} {result}')