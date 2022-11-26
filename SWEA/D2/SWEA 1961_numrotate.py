T = int(input())
def rotate(arr): #문자열 돌려주는 함수
    arrR = [[0]*N for _ in range(N)] #기존 배열을 돌린것을 저장할 N*N의 2차원 배열 만들기
    for i in range(N):
        for j in range(N):
            arrR[i][j] = arr[N-j-1][i] #90도 돌렸을때 규칙 찾기 
    return arrR

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    arr_90 = rotate(arr) #90도 
    arr_180 = rotate(arr_90) #90 + 90 180도
    arr_270 = rotate(arr_180) #180 + 90 270
    
    print(f'#{test_case}')
    for a,b,c in zip(arr_90,arr_180,arr_270): #출력의 경우 각 행별로 나와있으므로 zip으로 묶어서 반복
        print(f'{"".join(map(str,a))} {"".join(map(str,b))} {"".join(map(str,c))}') #문자열로 바꿔준다