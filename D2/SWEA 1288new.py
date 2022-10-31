T = int(input())

for test_case in range(1, T+1):
    cnt = 0
    N = int(input())
    listA = ''

    while True:
        cnt += 1 # cnt는 1씩 증가
        listA += str(N*cnt) #listA에 N*cnt를 문자형으로 전부 이어붙인다
        listB = ''.join(set(listA)) #set을 통해 listA의 중복값 제거

        if len(listB) == 10: #listB의 길이가 10이면 0 1 2 3 4 5 6 7 8 9 가 모두 들어감
            print(f'#{test_case} {N*cnt}')
            break

