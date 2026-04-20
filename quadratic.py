import math

def getNumber(prmpt): #숫자 입력
    while True: #숫자 입력할때까지 반복
        try:
            return float(input(prmpt)) #입력값 유리수 변환(유리수 맞나 암튼 까먹음)
        except ValueError: #오류나면
            print("insert a number") #숫자 아니면 경고

print("ax^2 + bx + c = 0")
a = getNumber("a: ")
b = getNumber("b: ")
c = getNumber("c: ")

if a == 0:
    print("a cannot be 0") #a=0이면 빠꾸
else:
    discrim = b**2 - 4*a*c #판별식 b^2 - 4ac
    if discrim > 0:
        root1 = (-b + math.sqrt(discrim)) / (2*a) #근1
        root2 = (-b - math.sqrt(discrim)) / (2*a) #근2
        
        print(f"first root: {-b / (2*a)} + sqrt({discrim}) / {(2*a)}")
        print(f"second root: {-b / (2*a)} - sqrt({discrim}) / {(2*a)}")
        print(f"two real roots: {root1}, {root2}") #판별식 양수면 서로 다른 두 실근
        
        if not root1.is_integer() or not root2.is_integer(): #정수로 안나오면
            print("what the hell is this") #숫자가 뭐고 이게
    elif discrim == 0:
        root = -b / (2*a) #중근
        print(f"real multiple root: {root}") #판별식 0이면 중근
    elif discrim < 0:
        real_part = -b / (2*a) #실부
        imag_part = math.sqrt(-discrim) / (2*a) #허부
        
        print(f"first root: {real_part} + sqrt({-discrim / (2*a)})i")
        print(f"second root: {real_part} - sqrt({-discrim / (2*a)})i")
        print(f"two imaginary roots: {real_part} + {imag_part}i, {real_part} - {imag_part}i") #판별식 음수면 서로 다른 두 허근  
        
        if not real_part.is_integer() or not imag_part.is_integer(): #정수로 안나오면
            print("what the hell is this") #숫자가 드럽다
    #분수로 표현 어케하지