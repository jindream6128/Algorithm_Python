T = int(input())
for i in range(1, T+1):
    kor_won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    kor_num = dict.fromkeys(kor_won, 0)
    #kor_won의 리스트를 키를 기준으로 딕셔너리 형태로 바꾼다.
    #kor_num = {500000:0 10000:0. 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}
    N = int(input())
    
    for a in kor_won: #kor_won 리스트를 순서대로 돈다
        kor_num[a] += N//a
        N %= a
    
    print(f'#{i}')
    for b in kor_won: #kor_num 의 동전 갯수 즉 동전 갯수 출력하기
        print(f'{kor_num[b]}', end=" ")
    print()