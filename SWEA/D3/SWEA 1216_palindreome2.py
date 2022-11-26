# file input
import sys
sys.stdin = open("input.txt", "r")

def is_pal(arr,leng):
    for lst in arr:
        for i in range(0, N-leng+1):
            if lst[i:i+leng] == lst[i:i+leng][::-1]:
                return True
def is_pal_best(arr,leng):
    for lst in arr:
        for i in range(0, N-leng+1):
            for j in range(leng//2):
                if lst[i+j] != lst[i+leng-1-j]:
                    break
            else:
                return True

for tc in range(1,11):
    _ = input()
    N = 100
    arr1 = [list(input()) for _ in range(N)]
    arr2 = [''.join(x) for x in zip(*arr1)]

    for leng in range(N, 1, -1):
        if is_pal_best(arr1,leng) or is_pal_best(arr2,leng):
            break
    print(f'#{tc} {leng}')