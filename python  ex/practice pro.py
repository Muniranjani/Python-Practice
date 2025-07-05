# 1.Find the Number is odd or even

# def num(a):
#     if(a%2==0):
#         print("The number is even")
#     else:
#         print("The number is odd")
# result=num(int(input("Enter the number: ")))
# print(result)

#2.Find the number is positive or negative

# def num(a):
#     if(a<0):
#         print("The number is negative")
#     elif(a==0):
#         print("The number is zero")
#     else:
#         print("The number is positive")
# result=num(int(input("Enter the number: ")))
# print(result)
    
#3.find the sum of two number
#type1
# def sum(a,b):
#     add=(a+b)
#     print(add)
# a1=int(input("1: "))
# b1=int(input("2: "))
# sum(a1,b1)

#type2
# def sum(a,b):
#     return a+b
# print(sum(int(input("Enter the number1 : ")),int(input("Enter the number2: "))))

#4.find the number is prime or not

# def num(a):
#    for i in range(2,a):
#         if(a%i==0):
#             print(a," is not a prime num ")
#         else:
#             print(a,"is a prime number")
# a=int(input("Enter the number: "))
# num(a)

#5.find maximum of two number
# def max(a,b):
#     if(a>b):
#         print(a,"is the maximum number")
#     else:
#         print(b,"is the maximum number")
# number=max(int(input("Enter the Number1: ")),int(input("Enter the number2: ")))

#6.find maximum of three number

# def max(a,b,c):
#     if(a>b):
#         print(a,"is maximum number")
#     elif(b>c):
#         print(b,"is maximum number")
#     else:
#         print(c,"is the maximum number")
# a=int(input("Enter the num1: "))
# b=int(input("Enter the num2: "))
# c=int(input("Enter the num3: "))
# max(a,b,c)

#7.find the factorial of the given number

# def fac(a):
#     factorial=1
#     for i in range(1,a+1):
#         factorial=factorial*i
#     if(a<0):
#         print("The factorial does'nt exist")
#     elif(a==0):
#         print("The given factorial is zero")
#     else:
#         print("The factorial of the",a, "is",factorial)
# n=fac(int(input("Enter the number: ")))

#8.print the star

# def fun(a):
#     for i in range(1,a+1):
#         for j in range(0,i):
#             print("*",end="")
#         print("")
# num=(fun(int(input("how many line pf star you will make: "))))

#9.print the triangle star

# def fun(a):
#    for i in range(0,a):
#       print(" "*(a-i-1),end="")
#       print("*"*(2*i+1))
# num=fun(int(input("Enter the number to make the triangle: ")))

#10.print the alphapet in ascending order

# def fun(a):
#     for i in range(1,a):
#         for j in range(65,65+i):
#             print(chr(j),end="")
#         print()
# fun(6)

# def fun(a):
#     for i in range(0,a):
#         print(" "*(a-i-1),end="")
#         print(chr(65+i)*(2*i+1))
# fun(5)

