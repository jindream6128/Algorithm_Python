T = int(input())

for test_case in range(1,T+1):
    ans = '' # 이어붙일 문자열 초기화
    N = int(input())
    for i in range(N):
        string, num = input().split() # 알파벳과, 숫자를 입력
        ans += string * int(num) #입력된 알파벳을 숫자만큼 반복하며 ans에 더하여 연결
    print(f'#{test_case}')
    for j in range(len(ans)//10+1): #  만약 ans의 길이가 37이라면 총 4번 반복하여 너비가 10인 문자열 3개와 남은 7 을 한줄로 출력해준다
        print(f'{ans[j*10:j*10+10]}') # 문자열 인덱싱 이용