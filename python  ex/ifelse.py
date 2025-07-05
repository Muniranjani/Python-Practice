salary=int(input("Enter the salary:"))
age=int(input("Enter the age:"))
if(salary>=20000 or age<=25):
    loan=int(input("enter the loan amount:"))
    if(loan>50000):
        print("Maximun loan amount is 50000")
    else:
        print("you are elgibile for loan")
    
else:
    print ("you are not elgibile for loan")
