s=input('Give a string also include "#" "%" "*" into the string: ')
print(s)
result=''
for x in s:
    if x.islower():
        result += x
    elif x == '*':
        result = result[0:len(result)-1:]
    elif x == '#':
        result = result*2
    elif x == '%':
        result = result[::-1]
    else:
        False
print(result)