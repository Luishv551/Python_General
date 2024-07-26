import sys

for linha in sys.stdin:
    a, b, c = map(int, linha.split())
    
    if b != a and b != c:
        print('B')
    elif a != b and a != c:
        print('A')
    elif c != a and c != b:
        print('C')
    else:
        print('*')
