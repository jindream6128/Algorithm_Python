import sys
sys.stdin = open("input.txt", 'r')
T = int(input())
for tc in range(1,T+1):
    lst = list(input())
    cnt =0
    for i in range(0, len(lst)):
        if lst[i] == '(':
            cnt += 1
        elif lst[i] == ')' and lst[i-1] != '(':
            cnt += 1

    print(f'#{tc} {cnt}')