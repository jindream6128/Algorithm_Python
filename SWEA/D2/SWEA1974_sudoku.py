# 이렇게 1과 0 이나오는건 함수로 만들어서 관리하면 편하다
def solve():
    #행 먼저
    for lst in arr:
        if len(set(lst)) != 9: #set함수를 활용하여 중복값을 삭제, 만약에 9가 아니라면 중복되는 값이 존재
            return 0
        
    #열을 전치행렬로 바꾸어 행으로 똑같이 계산
    #arr1 에 arr의 전치행렬 저장
    arr1 = list(zip(*arr))
    for lst in arr1:
        if len(set(lst)) != 9:
            return 0
    
    #이제 3*3의 블럭을 생각한다
    for i in range(0, 9, 3): #시작점의 x좌표 0 3 6 즉 0부터 9까지 3씩 증가한다
        for j in range(0,9,3): #시작점의 y좌표 0 3 6 동일
            #똑같이 리스트에 저장한다, 저장된 리스트를 행과,열과 동일하게 비교
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3] #한줄씩 리스트에 저장해서 총 크기가 9가 된다
            if len(set(lst)) != 9:
                return 0
        
    return 1 #모두 통과하면 1

T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    
    ans = solve()
    
    print(f"#{test_case} {ans}")