import math

print("\n실수범위의 인수분해를 해주는 프로그램 입니다.\n")
print("각 항의 계수는 정수만 입력해주세요.\n")

while True:
    a = input("\nx^2의 계수를 입력하세요 > ")
    try:
        a = int(a)
    except ValueError: # a 가 정수가 아니면 ValueError 발생 그러면 정수로 입력하라고 다시 안내
        print("\nx^2의 계수는 0이 아닌 정수로 입력하세요.")
    else:
        break

while True:
    b = input("\nx의 계수를 입력하세요 > ")
    try:
        b = int(b)
    except ValueError:
        print("\nx의 계수는 정수로 입력하세요.")
    else:
        break

while True:
    c = input("\n상수항을 입력하세요 > ")
    try:
        c = int(c)
    except ValueError:
        print("\n상수항은 정수를 입력하세요.")
    else:
        break

try:    
    root0 = (-b + math.sqrt(b**2 -4 * a * c)) / (2*a)

    root1 = (-b - math.sqrt(b**2 -4 * a * c)) / (2*a)
except ValueError:
    print("\n실수범위내의 인수분해만 가능합니다")
    print("\n다시 시도하세요.")
    exit()
except ZeroDivisionError:
    print("\nx^2의 계수가 0일경우 인수분해가 불가능합니다.")
    print("\n다시 시도하세요.")
    exit()


result = f"(x{int(root0)})(x{int(root1)})"

if root0 == root1 and root0 > 0:
    if type(root0) is int and type(root1) is int:
        result = f"(x-{int(root0)})^2"
    result = f"(x-{int(root0)})^2"

elif root0 == root1 and root0 < 0:
    root0 = -1*root0
    if type(root0) is int and type(root1) is int:
        root0 = -1*root0
        result == f"(x+{int(root0)})^2"
    result = f"(x+{int(root0)})^2"

elif root0 > 0 and root1 < 0:
    root1 = -1*root1
    result = f"(x-{float(root0)})(x+{float(root1)})"

elif root0 < 0 and root1 > 0:
    root0 = -1*root0
    result = f"(x+{float(root0)})(x-{float(root1)})"

elif root0 > 0 and root1 > 0: #2번 근이 모두 음수일때
    result = f"(x-{float(root0)})(x-{float(root1)})"

elif root0 < 0 and root1 < 0: # 1번 근이 모두 양수일때
    root0 = -1*root0
    root1 = -1*root1
    result = f"(x+{float(root0)})(x+{float(root1)})"

if a > 1 and root0 > 0 and root1 > 0: # 1번 근이 모두 양수
    if type(int(root0)) is int and type(int(root1)) is int:
        pass
    else:
        root0 = a * root0
        root1 = a * root1
    result = f"{a}(x+{float(root0)})(x+{float(root1)})"
    if type(int(root0)) is int and type(int(root1)) is int:
        result = f"{a}(x+{int(root0)})(x+{int(root1)})"
    else:
        result = f"{a}(x+{float(root0)})(x+{float(root1)})"

if a > 1 and root0 < 0 and root1 < 0: # 2번 근이 모두 음수
    result = f"{a}(x-{float(root0)})(x-{float(root1)})"
    if type(int(root0)) is int and type(int(root1)) is int:
        result = f"{a}(x-{int(root0)})(x-{int(root1)})"

print(f"\n계산결과는 > {result} 입니다!")
