def greater_num(a,b,c):
    if(a>b and a>c):
        print("a is greater number")
    elif(b>c):
        print("b is greater number")
    else:
        print("c is greater number")
n1=int(input("Enter the number1 : "))
n2=int(input("Enter the number2 : "))
n3=int(input("Enter the number3 : "))
greater_num(n1,n2,n3)