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


result = ""
if int(root0) == root0:
    root0 = int(root0)
if int(root1) == root1:
    root1 = int(root1)
if not a == 1:
    b /= a
    c /= a
    if a == -1:
        result = "-"        
    else:
        result = str(a)


if root0 == root1 and root0 > 0 :
    result += f"(x-{abs(root1)})^2"
    print(f"\n계산결과는 > {result} 입니다!")
    exit()

if root0 == root1 and root0 < 0 :
    result += f"(x+{abs(root1)})^2"
    print(f"\n계산결과는 > {result} 입니다!")
    exit()

if root0 > 0:
    result += f"(x-{root0})"
elif root0 < 0:
    result += f"(x+{abs(root0)})"
else:
    result += "x"

if root1 > 0:
    result += f"(x-{root1})"
elif root1 < 0:
    result += f"(x+{abs(root1)})"
else:
    result += "x"
print(f"\n계산결과는 > {result} 입니다!")
exit()
