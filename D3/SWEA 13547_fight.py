import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == 'o':
            cnt+=1

    if 15-len(lst)+cnt >= 8:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')