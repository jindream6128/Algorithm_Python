import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    num = list(map(int, input().split()))

    for i in range(len(num)):
        if num[i] < 40:
            num[i] = 40
        else:
            continue
    print(f'#{tc} {int(sum(num)/len(num))}')