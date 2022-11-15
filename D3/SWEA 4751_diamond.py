import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
     w = list(input())
     wl = len(w)
     a = '..#.'
     b = '.#'
     c = '.'
     d = '#'

     lst1 = a*wl + c
     lst2 = b*2*wl + c
     lst3 = ''
     for i in range(0,wl):
         lst3 += "#."+w[i]+"."

     print(lst1)
     print(lst2)
     print(lst3+d)
     print(lst2)
     print(lst1)