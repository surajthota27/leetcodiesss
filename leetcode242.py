def ValAna(s,t):
    if sorted(s)==sorted(t):
        return True
s=input('Enter a string: ')
t=input('Enter an another string: ')
print(ValAna(s,t))