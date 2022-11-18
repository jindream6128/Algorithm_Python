import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    a,b,c = map(int, input().split())
# 어떤 빵이든 상관 없이 그냥 많은 개수의 빵을 사는거기 때문에 더 작은걸로 c를 나눈 몫이 답이된다.
    if a >= b :
        a,b = b,a

    ans = c//a

    print(f'#{tc} {ans}')