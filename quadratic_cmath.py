import ast
import cmath #for sqrt and imaginary numbers

def getNumber(prompt): #getting a number
    while True:
        try:
            return complex(ast.literal_eval(input(prompt))) #allows user to input sqrt or imaginary numbers, which is very very good good
        except Exception: #if sth happens
            print("error: wtf u did that for?") #you sob, you broke the program

def is_integer(z): #is it integer
    return z.imag == 0 and z.real == int(z.real) #yup or nope

#getting numbers
print("ax^2 + bx + c = 0")
a = getNumber("a: ") 
b = getNumber("b: ")
c = getNumber("c: ")

if a == 0:
    print("a cannot be 0") #wtf
else:
    discrim = b**2 - 4*a*c #discrimination
    sqrt_discrim = cmath.sqrt(discrim) #sqrt
    divisor = 2*a #i dont think it is necessary. why tf i made this
    
    if discrim == 0: #multiple root
        root = -b / divisor
        print(f"real multiple root: {root}")
    else:
        root1 = (-b + sqrt_discrim) / divisor
        root2 = (-b - sqrt_discrim) / divisor
        
        print(f"first root: {-b / divisor} + sqrt({discrim}) / {divisor}")
        print(f"second root: {-b / divisor} - sqrt({discrim}) / {divisor}")
        
        if is_integer(root1) and is_integer(root2):
            print(f"two real roots: {int(root1.real)}, {int(root2.real)}") #if they are integers, print them.
        else:
            print(f"roots: {root1}, {root2}") #otherwise, print them as they are, such as complex numbers or imaginary numbers