import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # a,b,c = map(int, input().split())
    # if a==b==c:
    #     ans = a
    # elif a==b:
    #     ans =c
    # elif a==c:
    #     ans=b
    # elif b==c:
    #     ans=a

    lst = list(map(int, input().split()))
    for i in range(len(lst)):
        if lst.count(lst[i])==1 or lst.count(lst[i])==len(lst):
            ans = lst[i]
    print(f'#{tc} {ans}')