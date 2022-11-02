T = int(input())

for test_case in range(1,T+1):
    strA = input() # 문자열 입력
    # translate 메소드로 여러개 문자열 지우기
    # maketrans함수를 통해 table의 왼쪽에는 치환하고 싶은 문자, 오른쪽에는 새로운 문자를 저장한다
    table = strA.maketrans({
        'a': '',
        'e': '',
        'o': '',
        'i': '',
        'u': '',
    })
    # 출력의 겨우 strA.translate(table) strA의 문자열에서 table의 패턴을 적용시켜서 출력하여라
    print(f'#{test_case} {strA.translate(table)}')