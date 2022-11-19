import sys
sys.stdin =open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    d,h,m = map(int,input().split())
    if d == 11:
        if h < 11:
            ans = -1
        if h >= 11:
            ans = ((h*60)+m) - 671

    elif d > 11:
        ans = (d*24*60) + (h*60) + m - ((11*24*60) + (11*60) +11)

    print(f'#{tc} {ans}')