class X:
    pass
x = X()
x.x = 10
y = x
y.x = 12

print(x.x)