a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)
b=a
print(a==b)
print(a is b)
b[0]=5
print(a)
print(a[:])