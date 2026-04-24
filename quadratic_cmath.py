import cmath
import math

def getNumber(number): #숫자 입력
    while True: #숫자 입력할때까지 반복
        try:
            return complex(eval(input(number))) #입력값 유리수 변환(유리수 맞나 암튼 까먹음)
        except (ValueError, NameError): #오류나면(숫자 아니면)
            print("insert a number") #숫자 아니면 경고

print("ax^2 + bx + c = 0")
a = getNumber("a: ")
b = getNumber("b: ")
c = getNumber("c: ")

if a == 0:
    print("a cannot be 0") #a=0이면 빠꾸
else:
    discrim = b**2 - 4*a*c #판별식 b^2 - 4ac

    if discrim == 0:
        root = -b / (2*a) #중근
        print(f"real multiple root: {root}") #판별식 0이면 중근
    else:
        root1 = (-b + cmath.sqrt(discrim)) / (2*a) #근1
        root2 = (-b - cmath.sqrt(discrim)) / (2*a) #근2
        
        print(f"first root: {-b / (2*a)} + sqrt({discrim}) / {(2*a)}")
        print(f"second root: {-b / (2*a)} - sqrt({discrim}) / {(2*a)}")
        
        if (root1.imag == 0 and root1.real % 1 == 0) and (root2.imag == 0 and root2.real % 1 == 0): #정수 실근
            print(f"two real roots: {int(root1.real)}, {int(root2.real)}")
        else:
            print(f"roots: {root1}, {root2}") #정수 아니면