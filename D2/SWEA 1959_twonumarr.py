T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arrA = list(map(int,input().split()))
    arrB = list(map(int,input().split()))
    ans = 0
    # N이랑M 이 동일할때
    if N==M:
        for i in range(N):
            ans += arrA[i]*arrB[i]
    # N<M일때 -1의 인덱스로 계산해서 작은 배열의 끝부터 비교한다
    elif N<M:
        sum = [0]*(M-N+1)
        for i in range(0, M-N+1):
            for j in range(-1, -N-1, -1):
                sum[i] += arrA[j]*arrB[j-i]
        ans = max(sum)
    # N>M일때 로 비교
    elif N>M:
        sum = [0]*(N-M+1)
        for i in range(0, N-M+1):
            for j in range(-1, -M-1, -1):
                sum[i] += arrA[j-i]*arrB[j]
        ans = max(sum)
    # arrA, arrB의 원소들을 곱한 값을sum이라는 배열을 만들어, sum 배열에 저장한다
    # ans값에는 sum 리스트의 max값을 저장한다.
    print(f'#{test_case} {ans}')
            
# 같은 로직 나오는거 중복 지우기 
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     arrA = list(map(int,input().split()))
#     arrB = list(map(int,input().split()))
    
#     # N과 M이 항상 N < M 이 될 수 있도록 
#     if N > M:
#         arrA, arrB = arrB, arrA
#         N, M = M, N
        
#     sum = [0]*(M-N+1)
#     for i in range(0, M-N+1):
#         for j in range(-1, -N-1, -1):
#             sum[i] += arrA[j]*arrB[j-i]
#     print(f'#{test_case} {max(sum)}')     