"""
1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
13 14 15 PUM
17 18 19 PUM
21 22 23 PUM
25 26 27 PUM

"""

xpum = int(input())

numero = 1


for i in range (xpum):
    print(f"{numero} {numero+1} {numero+2} PUM")
    numero += 4