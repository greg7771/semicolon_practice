import math
print()
print("실수범위의 인수분해를 해주는 프로그램 입니다.")
print()
a = int(input("최고차항의 계수 > "))
b = int(input("x의 계수 > "))
c = int(input("상수항 > "))

root0 = (-b + math.sqrt(b**2 -4 * a * c)) / (2*a)

root1 = (-b - math.sqrt(b**2 -4 * a * c)) / (2*a)

result = f"(x{int(root0)})(x{int(root1)})"

if root0 == root1 and root0 > 0:
    result = f"(x-{float(root0)})^2"

elif root0 == root1 and root0 < 0:
    root0 = -1*root0
    result = f"(x+{float(root0)})^2"

elif root0 > 0 and root1 < 0:
    root1 = -1*root1
    result = f"(x-{float(root0)})(x+{float(root1)})"

elif root0 < 0 and root1 > 0:
    root0 = -1*root0
    result = f"(x+{float(root0)})(x-{float(root1)})"

elif root0 > 0 and root1 > 0:
    result = f"(x-{float(root0)})(x-{float(root1)})"

elif root0 < 0 and root1 < 0:
    root0 = -1*root0
    root1 = -1*root1
    result = f"(x+{float(root0)})(x+{float(root1)})"

print()
print(result)
