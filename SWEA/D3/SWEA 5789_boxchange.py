import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, Q = map(int,input().split())
    lst = []
    for _ in range(N):
        lst.append(0)

    for i in range(1,Q+1):
        L,R = map(int, input().split())
        for j in range(L-1, R):
            lst[j] = i
    #join은 문자열이여야 하기때문에 map으로 int형들을 str형으로 바꿔준다
    ans = ' '.join(map(str, lst))
    print(f'#{tc} {ans}')