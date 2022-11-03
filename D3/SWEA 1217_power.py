def power(a,n): # power (거듭제곱 함수 구현)
    ans = 1
    for _ in range(n):
        ans *= a
    return ans

for _ in range(10):
    T = int(input())
    a, n = map(int, input().split())
    print(f'#{T} {power(a,n)}')
