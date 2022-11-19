import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    dct = {} #점수 : 칼로리 딕셔너리로 저장
    r_dct = {} #칼로리: 점수 딕셔너리로 저장
    N, L = map(int, input().split())
    macl = 1000 #maxcal 1000
    for _ in range(N):
        a,b = map(int, input().split())
        dct[a] = b
        r_dct[b] = a
