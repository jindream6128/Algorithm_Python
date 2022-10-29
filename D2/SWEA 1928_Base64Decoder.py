decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/'
          ] # 디코더 표
T = int(input())

for test_case in range(1,T+1):
    #인코딩된 암호문을 입력 받는다
    word = list(input())
    #인코딩된 암호문의 길이 
    word_len = len(word)
    
    # word 글자 -> 디코더 표에 대응하는 숫자
    # 디코더 표에 대응한느 숫자 -> 이진수 -> 이진수가 6자리가 아니면 0으로 채워줘야함
    mid = ''
    
    for a in range(word_len):
        #word 글자 -> 디코더 표의 숫자
        num = decode.index(word[a])
        
        #디코더 표의 숫자 2진수로 변환 -> 2진수 이므로 0b를 없애준다 -> 2번째 자리부터 끝까지 출력 
        # -> 6자리가 아니라면 앞에 0을 붙여주기위해 str로 바꾼다
        binary_num = str(bin(num)[2:])
        # 길이가 6이 아니면 즉 6자리가 아니면 반복문 실행
        # 앞에 0을 붙여준다
        while len(binary_num)<6:
            binary_num = '0' + binary_num
        # mid에 6자리 이진수를 전부 이어붙인다
        mid += binary_num
    #구하고자 하는 문장
    ans = ''
    #원래 글자 * 6bit // 8bit -> 한글자당 6bit가 나오고 그걸 8bit 로 쪼개서 다시 ASCII코드로 만든다
    for b in range(word_len*6//8):
        # 2진수에서 -> 10진수 변환 int(문자열, 2)
        
        #8bit씩 조개기 -> 10진수 변환
        cut = int(mid[b*8:b*8+8],2)
        #아스키코드 변환
        ans += chr(cut)

    print(f'#{test_case} {ans}')
        
#라이브러리 사용했을때
# import base64

# T = int(input())
# for test_case in range(1, T+1):
#     de = input()
#     answer = base64.b64decode(de).decode("UTF-8")
#     print(f'#{test_case} {answer}')