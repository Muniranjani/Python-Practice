def calculate(a,b):
    add=(a+b)
    sub=(a-b)
    mul=(a*b)
    div=(a/b)
    mod=(a%b)
    return add,sub,mul,div,mod

num1=int(input("Enter the number1 : "))
num2=int(input('Enter the number2 : '))
a,s,m,d,m=calculate(num1,num2)
print("Addition : ", a)
print("Subraction : ", s)
print("Multiplication : ", m)
print("Division : ", d)
print("Modulus : ", m)