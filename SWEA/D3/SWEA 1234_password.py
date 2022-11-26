import sys
sys.stdin =open("input.txt", "r")

for tc in range(1,11):
    num, lst = input().split()
    num = int(num)
    lst = list(lst)
    i=0

    while True:
            if lst[i] == lst[i+1]:
                del lst[i:i+2]
                num -= 2
                i -= 2
            i += 1
            if i == num-1:
                break

    ans = ''.join(lst)
    print(f'#{tc} {ans}')