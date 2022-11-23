#If15. Даны три числа. Найти сумму двух наибольших из них.

a, b, c = map(int, input().split())
if a <= c and a <= b:
    print(c + b)
elif b <= c and b <= a:
    print(c + a)
elif c <= b and c <= a:
    print(a + b)
