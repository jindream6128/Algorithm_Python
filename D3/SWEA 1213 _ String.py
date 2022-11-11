# file input
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11):
    _ = input()
    fstr = input()
    astr = input()

    ans = astr.count(fstr)
    print(f'#{tc} {ans}')