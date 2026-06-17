def ProcessStr(s,k):
    lengths=[]
    length=0
    for x in s:
        if x.isalpha():
            length+=1  #k1
        elif x == '*':
            length-=1  #k2
        elif x == '#':
            length=length*2   #k2*2=k3
        elif x == '%':
            pass
    if k>=length:
        return '.'
    else:
        lengths.append(length)

        if k >= length:
            return '.'

        # Backward pass
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            curr_len = lengths[i]
            prev_len = lengths[i - 1] if i > 0 else 0

            if ch == '%':
                k = curr_len - 1 - k

            elif ch == '#':
                k %= prev_len

            elif ch == '*':
                # deletion only affected the last character
                pass

            elif ch.islower():
                if k == curr_len - 1:
                    return ch

        return '.'
print(ProcessStr('z*#',0))