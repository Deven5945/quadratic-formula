import math

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("숫자를 입력하세요")

print("ax^2 + bx + c = 0")
a = get_number("a: ")
b = get_number("b: ")
c = get_number("c: ")

if a == 0:
    print("a는 0이 될 수 없습니다")
else:
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        
        print(f"두 실근: {root1}, {root2}")
        print(f"근의 공식 형태: ({-b} ± √{discriminant}) / {2*a}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"중근: {root}")
    elif discriminant < 0:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        
        print(f"두 허근: {real_part} + {imag_part}i, {real_part} - {imag_part}i")
        print(f"근의 공식 형태: ({-b} ± √{-discriminant}i) / {2*a}")