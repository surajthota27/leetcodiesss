x=123
if x<(2**(31))-1:
    y=str(x)
    z=int(y[::-1])
    print(z)
else:
    print(0)
    