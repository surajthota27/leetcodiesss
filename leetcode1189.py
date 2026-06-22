str='balloon'
s=sorted(str)
print(s)
text="balllllllllllloooooooooon"
s1=sorted(text)
result=[x for x in s if x in s1]
print(result)
if s==result and str.count('l')<=text.count('l') and str.count('o')<=text.count('o'):
    a=text.count('b')
    print(a)
else:
    print('0')