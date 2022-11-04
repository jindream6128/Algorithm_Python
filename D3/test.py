def dfs(nth):
    print('  ' * nth, f'dfs({nth}), permutation=', permutation)

    if nth == r: # dfs의 레벨이 r과 같을때 (permutation이 완성되었을 때)
        print('  ' * nth, '완성! -> ', permutation) # 종료 조건일때 permutation 출력
        return

    for number in n:  # n의 각 number마다 반복
      if number in permutation: # [1,1,1] 이런식으로 만드는걸 방지하기 위해 한번 쓴 숫자인지 확인
        continue

      permutation.append(number) # [1,3] 에서 [1,3,2] 식으로 하나 추가
      dfs(nth + 1) # 현재 permutation이 미완성이면 완성을 위해 더 깊게 호출
      permutation.pop() # [1,3,2] 에서 [1,3] 으로 빼고 다음 루프에서 [1,3,4]이런식으로 만들어 진행


n = [1,2,3]
r = 2
permutation = []

dfs(0)