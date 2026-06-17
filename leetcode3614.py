#Memory limit Exceeded.
class MyIndexError(Exception):
    pass
def leetcode(s,k):
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
        if k>=len(result):
            raise MyIndexError('-')
        else:
            return result[k]
try:
    leetcode('z*#',0)
except MyIndexError as e:
    print(e)
    