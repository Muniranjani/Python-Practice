def is_leap(a):
    if(a%4==0):
        print("True")
    else:
        print("False")
year = int(input())
print(is_leap(year))