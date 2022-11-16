import sys
sys.stdin = open("input.txt", "r")
# 문제가 이상함,,, USB를 두번 꽂는?? Why??
T = int(input())
for tc in range(1,T+1):
    p, q = map(float, input().split())

    s1 = (1-p)*q
    s2 = p*(1-q)*q
    if s1<s2:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')