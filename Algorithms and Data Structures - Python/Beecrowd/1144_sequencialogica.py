"""
1 1 1
1 2 2
2 4 8
2 5 9
3 9 27
3 10 28
4 16 64
4 17 65
5 25 125
5 26 126


LOGICA:

1 1^2 1^3

1 1^2 + 1 1^3 + 1

2 2^2 2^3

2 2^2 +1 2^3 +1
.
.
.

"""

n = int(input())
num = 1

for i in range (n):
    n2 = num ** 2
    n3 = num ** 3

    print(f"{num} {n2} {n3}")
    print(f"{num} {n2 + 1} {n3 + 1}")

    num+=1
