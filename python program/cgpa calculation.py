def cgpa(a):
    if(a<=10 and a>=9):
        print("O Grade")
    elif(a<=9 and a>=8):
        print("A+ Grade")
    elif(a<=8 and a>=7):
        print("A grade")
    elif(a<=7 and a>=6):
        print("B+ Grade")
    elif(a<=6 and a>=5):
        print("B Grade")
    else:
        print("Fail")
input=float(input("Enter your CGPA: "))
cgpa(input)
