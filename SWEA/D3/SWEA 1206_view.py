#file input
# import sys
# sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    high = list(map(int, input().split()))
    ans = []
    mid = 0

    for i in range(2,N-2):
        left1 = high[i]-high[i-1]
        left2 = high[i]-high[i-2]
        right1 = high[i]-high[i+1]
        right2 = high[i]-high[i+2]

        if left1 > 0 and left2 > 0 and right1 > 0 and right2 > 0 :
            mid= min(left1, left2, right1, right2)
            ans.append(mid)

    print(f'#{test_case} {sum(ans)}')
