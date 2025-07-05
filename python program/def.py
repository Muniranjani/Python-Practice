x="global"
def f3():
    global x
    y="local"
    x=x*5
    print(x)
    print(y)
f3()