import sys
sys.stdin = open("input.txt", "r")

T=int(input())
for tc in range(1,T+1):
    st = list(input())
    num = int(input())
    location = list(map(int,input().split()))
    location.sort(reverse=True)
    for i in location:
        st.insert(i, '-')

    ans = ''.join(st)
    print(f'#{tc} {ans}' )