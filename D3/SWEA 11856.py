import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    st = list(input())
    result = list(set(st))
    if len(result) == 2 and st.count(result[0]) == 2 and st.count(result[1]) ==2:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')