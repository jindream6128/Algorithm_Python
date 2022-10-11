T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.remove(max(arr)) #최대값 제거
    arr.remove(min(arr)) #최소값 제거
    arr_avg = round(sum(arr) / len(arr)) #소수점 첫번째 자리에서 반올림
    print("#{} {}".format(test_case, arr_avg))