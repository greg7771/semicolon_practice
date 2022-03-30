a = int(input("최고차항의 계수 > "))
b = int(input("x의 계수 > "))
c = int(input("상수항 > "))

x_ask = int(input("x에 대입할 수를 입력하세요 > "))
x = x_ask
def f():
    return a * (x **2) + b * x + c

print("정답은!")
print()
print((a * (x**2) + b * x + c))
print()
print("입니다~")

# if ask == "y" or "Y":
#     print()
#     print("계산 결과는")
#     print()
#     print((f()))
# if ask == "n" or "N":
#     print("다시 시도하세요")
