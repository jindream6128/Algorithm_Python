T = int(input())
for i in range(1, T+1):
    N = int(input())
    N_li = list(map(int, input().split()))
    N_li.sort() #python의 sort 함수로 오름차순 정렬 한다.
    print(f'#{i}', end=' ')
    
    for a in range(N):
        print(f'{N_li[a]}', end=' ') # 오름차순 정렬 된 N_li를 반복문을 통해 한개씩 출력하고, 하나출력한 뒤에는 공백을 넣어준다
    print() # 각 테스트 케이스별로 구분해야한다.