
def dfs(n):
    global ans
    if n == N: #n이 N번 교환하면 끝
        ans = max(ans, int("".join(map(str,lst))))
        return
        #L개 중에서 2개 뽑는 조합 (이후 둘을 교환)
        #1,2,3,4,5 => i가 1일때 2 3 4 5 가능 i가 2일때 3 4 5 가능
    for i in range(0, L-1):
        for j in range(i+1, L):
            lst[i], lst[j] =lst[j], lst[i] #(2개 뽑아서 2개 교환)
            chk = int("".join(map(str,lst))) #list형의 lst-> str형의 lst -> int형의 lst로 바꿔준다
            if (n,chk) not in v: #시간을 줄이기 위하여 기존에 돌았던 lst라면 돌지않고, 기존에 돌지 않았던 리스트는 돈다
                                # ex 8 -> 8,8 두가지가 선택이 가능한데 뭘선택하도 동일하다, 이럴땐 필요 없음
                dfs(n+1)    #재귀
                v.append((n, chk)) # 확인을 위하여 몇번 교환 해야하는지 n과 chk를 v확인용 list에 넣어준다

            lst[i],lst[j] = lst[j],lst[i] # 반드시 원상복구 시켜주기

T = int(input())
for tc in range(1,T+1):
    st ,t = input().split() #st는 맨처음 입력받는걸 문자열로, t는 몇회 바꿀껀지
    N = int(t) # t를 문자열로 입력 받았으니까 정수형 N으로 바꿔준다
    lst = [] #lst는 입력받은 문자열을 넣을 리스트
    for ch in st:
        lst.append(int(ch)) #각 문자열 요소들을 리스트에 넣어서 list로 만들어 주는거 정수형 리스트
    L = len(lst) #입력받은 문자열의 길이 L
    ans = 0 #최댓값은 정수형으로 저장될 꺼니까 0 으로 선언
    v = [] #돌았던 리스트인지 확인하기 위해서
    dfs(0)
    print(f'#{tc} {ans}')