a = int(input("최고차항의 계수 > "))
b = int(input("x의 계수 > "))
c = int(input("상수항 > "))


def f(x):
    return a * (x **2) + b * x + c

def factorization():
    -b