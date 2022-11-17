import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt =0
    for i in range (1,n-1):
        a, b, c = lst[i-1], lst[i], lst[i+1]
        if max(a,b,c) != b and min(a,b,c) != b:
            cnt +=1
    print(f'#{tc} {cnt}')